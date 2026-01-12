#!/usr/bin/env python3
"""
BigQuery MCP Server
Week 6 Day 3-4: BigQuery MCP統合用カスタムMCPサーバー

This MCP server provides tools to interact with Google BigQuery:
- List datasets
- List tables in a dataset
- Execute SQL queries
- Get table schema
- Insert data into tables

Setup:
1. Create GCP Service Account with BigQuery roles
2. Download JSON key file
3. Set GOOGLE_APPLICATION_CREDENTIALS environment variable
4. Set GCP_PROJECT_ID environment variable

Usage:
  python3 scripts/mcp_servers/bigquery_server.py
"""

import json
import os
import re
import sys
from typing import Any, Dict, List, Optional

# BigQuery imports
try:
    from google.cloud import bigquery
    from google.oauth2 import service_account
except ImportError:
    print("Error: google-cloud-bigquery not installed", file=sys.stderr)
    print("Install with: pip install google-cloud-bigquery", file=sys.stderr)
    sys.exit(1)


class BigQueryMCPServer:
    """MCP Server for BigQuery operations"""

    def __init__(self):
        # Load environment variables
        credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        self.project_id = os.getenv("GCP_PROJECT_ID")

        if not credentials_path:
            raise ValueError("GOOGLE_APPLICATION_CREDENTIALS environment variable not set")

        if not self.project_id:
            raise ValueError("GCP_PROJECT_ID environment variable not set")

        # Initialize BigQuery client
        if credentials_path and os.path.exists(credentials_path):
            credentials = service_account.Credentials.from_service_account_file(
                credentials_path
            )
            self.client = bigquery.Client(
                credentials=credentials, project=self.project_id
            )
        else:
            # Use default credentials
            self.client = bigquery.Client(project=self.project_id)

    def list_datasets(self) -> Dict[str, Any]:
        """List all datasets in the project"""
        try:
            datasets = list(self.client.list_datasets())
            result = []
            for dataset in datasets:
                result.append({
                    "dataset_id": dataset.dataset_id,
                    "full_dataset_id": dataset.full_dataset_id,
                    "project": dataset.project,
                })
            return {"datasets": result}
        except Exception as e:
            return {"error": str(e)}

    def list_tables(self, dataset_id: str) -> Dict[str, Any]:
        """List all tables in a dataset"""
        try:
            dataset_ref = self.client.dataset(dataset_id)
            tables = list(self.client.list_tables(dataset_ref))
            result = []
            for table in tables:
                result.append({
                    "table_id": table.table_id,
                    "full_table_id": table.full_table_id,
                    "table_type": table.table_type,
                })
            return {"tables": result}
        except Exception as e:
            return {"error": str(e)}

    def _validate_query(self, query: str) -> bool:
        """
        Validate SQL query to prevent SQL injection and dangerous operations.

        Returns True if query is safe, raises ValueError otherwise.
        """
        # Convert to uppercase for pattern matching
        query_upper = query.upper()

        # Dangerous SQL patterns to block
        dangerous_patterns = [
            r'--',                    # SQL comments
            r'/\*',                   # Multi-line comments
            r';\s*DROP',              # DROP statements
            r';\s*DELETE',            # DELETE statements without WHERE (dangerous)
            r';\s*TRUNCATE',          # TRUNCATE statements
            r';\s*ALTER',             # ALTER statements
            r';\s*EXEC',              # EXEC statements
            r';\s*EXECUTE',           # EXECUTE statements
            r'INFORMATION_SCHEMA',    # Schema introspection
            r'GRANT\s+',              # GRANT statements
            r'REVOKE\s+',             # REVOKE statements
        ]

        for pattern in dangerous_patterns:
            if re.search(pattern, query_upper):
                raise ValueError(f"Query contains potentially dangerous pattern: {pattern}")

        return True

    def execute_query(self, query: str, max_results: int = 100) -> Dict[str, Any]:
        """Execute a SQL query and return results"""
        try:
            # Validate query for SQL injection
            self._validate_query(query)

            query_job = self.client.query(query)
            # Add timeout to prevent long-running queries
            results = query_job.result(max_results=max_results, timeout=300)

            # Convert results to list of dicts
            rows = []
            for row in results:
                rows.append(dict(row))

            return {
                "total_rows": results.total_rows,
                "rows_returned": len(rows),
                "rows": rows,
                "schema": [{"name": field.name, "type": field.field_type} for field in results.schema],
            }
        except ValueError as e:
            # SQL injection validation error
            return {"error": f"Query validation failed: {str(e)}"}
        except Exception as e:
            return {"error": str(e)}

    def get_table_schema(self, dataset_id: str, table_id: str) -> Dict[str, Any]:
        """Get the schema of a table"""
        try:
            table_ref = self.client.dataset(dataset_id).table(table_id)
            table = self.client.get_table(table_ref)

            schema = []
            for field in table.schema:
                schema.append({
                    "name": field.name,
                    "type": field.field_type,
                    "mode": field.mode,
                    "description": field.description or "",
                })

            return {
                "dataset_id": dataset_id,
                "table_id": table_id,
                "num_rows": table.num_rows,
                "num_bytes": table.num_bytes,
                "schema": schema,
            }
        except Exception as e:
            return {"error": str(e)}

    def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incoming MCP tool requests"""
        method = request.get("method")
        params = request.get("params", {})

        if method == "tools/list":
            # Return list of available tools
            return {
                "tools": [
                    {
                        "name": "list_datasets",
                        "description": "List all datasets in the GCP project",
                        "inputSchema": {
                            "type": "object",
                            "properties": {},
                        },
                    },
                    {
                        "name": "list_tables",
                        "description": "List all tables in a dataset",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "dataset_id": {
                                    "type": "string",
                                    "description": "Dataset ID",
                                },
                            },
                            "required": ["dataset_id"],
                        },
                    },
                    {
                        "name": "execute_query",
                        "description": "Execute a SQL query and return results",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "query": {
                                    "type": "string",
                                    "description": "SQL query to execute",
                                },
                                "max_results": {
                                    "type": "integer",
                                    "description": "Maximum number of results to return (default: 100)",
                                    "default": 100,
                                },
                            },
                            "required": ["query"],
                        },
                    },
                    {
                        "name": "get_table_schema",
                        "description": "Get the schema of a table",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "dataset_id": {
                                    "type": "string",
                                    "description": "Dataset ID",
                                },
                                "table_id": {
                                    "type": "string",
                                    "description": "Table ID",
                                },
                            },
                            "required": ["dataset_id", "table_id"],
                        },
                    },
                ]
            }

        elif method == "tools/call":
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})

            if tool_name == "list_datasets":
                return self.list_datasets()
            elif tool_name == "list_tables":
                return self.list_tables(tool_args.get("dataset_id"))
            elif tool_name == "execute_query":
                return self.execute_query(
                    tool_args.get("query"), tool_args.get("max_results", 100)
                )
            elif tool_name == "get_table_schema":
                return self.get_table_schema(
                    tool_args.get("dataset_id"), tool_args.get("table_id")
                )
            else:
                return {"error": f"Unknown tool: {tool_name}"}

        else:
            return {"error": f"Unknown method: {method}"}


def main():
    """Main entry point for MCP server (stdio transport)"""
    try:
        server = BigQueryMCPServer()

        # Read JSON-RPC requests from stdin
        for line in sys.stdin:
            try:
                request = json.loads(line.strip())
                response = server.handle_request(request)

                # Write JSON-RPC response to stdout
                print(json.dumps(response), flush=True)

            except json.JSONDecodeError as e:
                error_response = {"error": f"Invalid JSON: {str(e)}"}
                print(json.dumps(error_response), flush=True)

            except Exception as e:
                error_response = {"error": f"Internal error: {str(e)}"}
                print(json.dumps(error_response), flush=True)

    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
