#!/usr/bin/env python3
"""
Sentry MCP Server
Week 6 Day 5-6: Sentry MCP統合用カスタムMCPサーバー

This MCP server provides tools to interact with Sentry:
- List projects
- Get recent issues
- Get issue details
- Resolve/ignore issues
- Get error statistics

Setup:
1. Go to Sentry Settings > Developer Settings > Auth Tokens
2. Create new token with scopes: event:read, project:read, org:read
3. Set SENTRY_AUTH_TOKEN environment variable
4. Set SENTRY_ORG_SLUG environment variable

Usage:
  python3 scripts/mcp_servers/sentry_server.py
"""

import json
import os
import sys
from typing import Any, Dict, List, Optional
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


class SentryMCPServer:
    """MCP Server for Sentry operations"""

    def __init__(self):
        # Load environment variables
        self.auth_token = os.getenv("SENTRY_AUTH_TOKEN")
        self.org_slug = os.getenv("SENTRY_ORG_SLUG")

        if not self.auth_token:
            raise ValueError("SENTRY_AUTH_TOKEN environment variable not set")

        if not self.org_slug:
            raise ValueError("SENTRY_ORG_SLUG environment variable not set")

        self.base_url = "https://sentry.io/api/0"

    def _make_request(self, endpoint: str, method: str = "GET", data: Optional[Dict] = None) -> Dict[str, Any]:
        """Make HTTP request to Sentry API"""
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.auth_token}",
            "Content-Type": "application/json",
        }

        try:
            if data:
                data_bytes = json.dumps(data).encode("utf-8")
                request = Request(url, data=data_bytes, headers=headers, method=method)
            else:
                request = Request(url, headers=headers, method=method)

            with urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))

        except HTTPError as e:
            error_body = e.read().decode("utf-8")
            try:
                error_data = json.loads(error_body)
                return {"error": error_data.get("detail", str(e))}
            except json.JSONDecodeError:
                return {"error": f"HTTP {e.code}: {error_body}"}

        except URLError as e:
            return {"error": f"Network error: {str(e)}"}

        except Exception as e:
            return {"error": f"Request failed: {str(e)}"}

    def list_projects(self) -> Dict[str, Any]:
        """List all projects in the organization"""
        try:
            result = self._make_request(f"/organizations/{self.org_slug}/projects/")

            if "error" in result:
                return result

            projects = []
            for project in result:
                projects.append({
                    "id": project.get("id"),
                    "slug": project.get("slug"),
                    "name": project.get("name"),
                    "platform": project.get("platform"),
                    "status": project.get("status"),
                })

            return {"projects": projects}

        except Exception as e:
            return {"error": str(e)}

    def get_recent_issues(self, project_slug: str, limit: int = 25) -> Dict[str, Any]:
        """Get recent issues for a project"""
        try:
            endpoint = f"/projects/{self.org_slug}/{project_slug}/issues/?statsPeriod=24h&limit={limit}"
            result = self._make_request(endpoint)

            if "error" in result:
                return result

            issues = []
            for issue in result:
                issues.append({
                    "id": issue.get("id"),
                    "title": issue.get("title"),
                    "status": issue.get("status"),
                    "level": issue.get("level"),
                    "count": issue.get("count"),
                    "userCount": issue.get("userCount"),
                    "firstSeen": issue.get("firstSeen"),
                    "lastSeen": issue.get("lastSeen"),
                    "permalink": issue.get("permalink"),
                })

            return {"issues": issues}

        except Exception as e:
            return {"error": str(e)}

    def get_issue_details(self, issue_id: str) -> Dict[str, Any]:
        """Get detailed information about an issue"""
        try:
            result = self._make_request(f"/issues/{issue_id}/")

            if "error" in result:
                return result

            # Extract key information
            details = {
                "id": result.get("id"),
                "title": result.get("title"),
                "status": result.get("status"),
                "level": result.get("level"),
                "count": result.get("count"),
                "userCount": result.get("userCount"),
                "firstSeen": result.get("firstSeen"),
                "lastSeen": result.get("lastSeen"),
                "permalink": result.get("permalink"),
                "metadata": result.get("metadata", {}),
                "tags": result.get("tags", []),
            }

            # Get latest event
            if result.get("lastEvent"):
                details["lastEvent"] = {
                    "id": result["lastEvent"].get("id"),
                    "message": result["lastEvent"].get("message"),
                    "platform": result["lastEvent"].get("platform"),
                }

            return details

        except Exception as e:
            return {"error": str(e)}

    def update_issue_status(self, issue_id: str, status: str) -> Dict[str, Any]:
        """Update issue status (resolved, ignored, unresolved)"""
        try:
            valid_statuses = ["resolved", "unresolved", "ignored"]
            if status not in valid_statuses:
                return {"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"}

            data = {"status": status}
            result = self._make_request(f"/issues/{issue_id}/", method="PUT", data=data)

            if "error" in result:
                return result

            return {
                "success": True,
                "id": result.get("id"),
                "status": result.get("status"),
            }

        except Exception as e:
            return {"error": str(e)}

    def get_stats(self, project_slug: str) -> Dict[str, Any]:
        """Get error statistics for a project"""
        try:
            # Get project details
            project_result = self._make_request(f"/projects/{self.org_slug}/{project_slug}/")

            if "error" in project_result:
                return project_result

            # Get issues stats
            issues_result = self._make_request(
                f"/projects/{self.org_slug}/{project_slug}/issues/?statsPeriod=24h"
            )

            if "error" in issues_result:
                return issues_result

            # Calculate stats
            total_events = sum(issue.get("count", 0) for issue in issues_result)
            total_users_affected = sum(issue.get("userCount", 0) for issue in issues_result)
            unresolved_count = len([i for i in issues_result if i.get("status") == "unresolved"])

            return {
                "project": {
                    "slug": project_result.get("slug"),
                    "name": project_result.get("name"),
                    "platform": project_result.get("platform"),
                },
                "stats_24h": {
                    "total_issues": len(issues_result),
                    "unresolved_issues": unresolved_count,
                    "total_events": total_events,
                    "users_affected": total_users_affected,
                },
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
                        "name": "list_projects",
                        "description": "List all projects in the Sentry organization",
                        "inputSchema": {
                            "type": "object",
                            "properties": {},
                        },
                    },
                    {
                        "name": "get_recent_issues",
                        "description": "Get recent issues for a project (last 24 hours)",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "project_slug": {
                                    "type": "string",
                                    "description": "Project slug",
                                },
                                "limit": {
                                    "type": "integer",
                                    "description": "Maximum number of issues to return (default: 25)",
                                    "default": 25,
                                },
                            },
                            "required": ["project_slug"],
                        },
                    },
                    {
                        "name": "get_issue_details",
                        "description": "Get detailed information about a specific issue",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "issue_id": {
                                    "type": "string",
                                    "description": "Issue ID",
                                },
                            },
                            "required": ["issue_id"],
                        },
                    },
                    {
                        "name": "update_issue_status",
                        "description": "Update issue status (resolved, ignored, unresolved)",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "issue_id": {
                                    "type": "string",
                                    "description": "Issue ID",
                                },
                                "status": {
                                    "type": "string",
                                    "description": "New status",
                                    "enum": ["resolved", "unresolved", "ignored"],
                                },
                            },
                            "required": ["issue_id", "status"],
                        },
                    },
                    {
                        "name": "get_stats",
                        "description": "Get error statistics for a project (last 24 hours)",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "project_slug": {
                                    "type": "string",
                                    "description": "Project slug",
                                },
                            },
                            "required": ["project_slug"],
                        },
                    },
                ]
            }

        elif method == "tools/call":
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})

            if tool_name == "list_projects":
                return self.list_projects()
            elif tool_name == "get_recent_issues":
                return self.get_recent_issues(
                    tool_args.get("project_slug"), tool_args.get("limit", 25)
                )
            elif tool_name == "get_issue_details":
                return self.get_issue_details(tool_args.get("issue_id"))
            elif tool_name == "update_issue_status":
                return self.update_issue_status(
                    tool_args.get("issue_id"), tool_args.get("status")
                )
            elif tool_name == "get_stats":
                return self.get_stats(tool_args.get("project_slug"))
            else:
                return {"error": f"Unknown tool: {tool_name}"}

        else:
            return {"error": f"Unknown method: {method}"}


def main():
    """Main entry point for MCP server (stdio transport)"""
    try:
        server = SentryMCPServer()

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
