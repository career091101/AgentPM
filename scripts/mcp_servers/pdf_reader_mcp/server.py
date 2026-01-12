"""PDF Reader MCP Server - stdio通信ベースのMCPサーバー"""

# ========================================
# 重要: MCPはstdioでJSON-RPC通信を行うため、
# 警告メッセージがstdoutに出力されると通信が壊れる。
# importの前に全ての警告を抑制する必要がある。
# ========================================
import warnings
import os
import sys

# 全ての警告を抑制
warnings.filterwarnings("ignore")

# 環境変数でも警告を抑制
os.environ["PYTHONWARNINGS"] = "ignore"

# stderrをNullにリダイレクト（警告がstderrに出力される場合の対策）
# ただしエラーは後でstderrに出力したいので、元のstderrを保存
_original_stderr = sys.stderr

import json
import asyncio
from pathlib import Path
from typing import Optional, Any

# stderrを元に戻す
sys.stderr = _original_stderr

from .config import get_config
from .pdf_processor import PDFProcessor
from .vision_analyzer import VisionAnalyzer
from .markdown_utils import (
    page_to_markdown,
    create_report_header,
    create_summary_section,
)


class PDFReaderMCPServer:
    """PDF Reader MCP Server"""
    
    def __init__(self):
        self.processor = PDFProcessor()
        self._analyzer: Optional[VisionAnalyzer] = None
        self.config = get_config()
    
    @property
    def analyzer(self) -> VisionAnalyzer:
        """Vision解析器を遅延初期化で取得"""
        if self._analyzer is None:
            self._analyzer = VisionAnalyzer()
        return self._analyzer
    
    def get_tools(self) -> list[dict]:
        """利用可能なツール一覧を返す"""
        return [
            {
                "name": "read_pdf",
                "description": "PDFファイルを読み込み、テキストと画像の解析結果をMarkdown形式で返します。",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "PDFファイルの絶対パス"
                        },
                        "start_page": {
                            "type": "integer",
                            "description": "開始ページ番号（1から始まる）",
                            "default": 1
                        },
                        "end_page": {
                            "type": "integer",
                            "description": "終了ページ番号（省略時は最終ページまで）"
                        },
                        "analyze_images": {
                            "type": "boolean",
                            "description": "画像をVision APIで解析するかどうか",
                            "default": True
                        }
                    },
                    "required": ["file_path"]
                }
            },
            {
                "name": "read_pdf_pages",
                "description": "PDFの指定したページのみを読み込みます。",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "PDFファイルの絶対パス"
                        },
                        "pages": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "読み込むページ番号のリスト（1から始まる）"
                        },
                        "analyze_images": {
                            "type": "boolean",
                            "description": "画像をVision APIで解析するかどうか",
                            "default": True
                        }
                    },
                    "required": ["file_path", "pages"]
                }
            },
            {
                "name": "get_pdf_info",
                "description": "PDFファイルの基本情報を取得します。",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "PDFファイルの絶対パス"
                        }
                    },
                    "required": ["file_path"]
                }
            },
            {
                "name": "extract_text_only",
                "description": "PDFからテキストのみを抽出します（画像解析なし、高速）。",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "PDFファイルの絶対パス"
                        },
                        "start_page": {
                            "type": "integer",
                            "description": "開始ページ番号",
                            "default": 1
                        },
                        "end_page": {
                            "type": "integer",
                            "description": "終了ページ番号"
                        }
                    },
                    "required": ["file_path"]
                }
            }
        ]
    
    async def read_pdf(
        self,
        file_path: str,
        start_page: int = 1,
        end_page: Optional[int] = None,
        analyze_images: bool = True
    ) -> str:
        """PDFを読み込みMarkdown形式で返す"""
        try:
            doc = self.processor.open(file_path)
            total_pages = self.processor.get_page_count(doc)
            
            actual_end = min(end_page, total_pages) if end_page else total_pages
            actual_start = max(1, start_page)
            
            markdown_parts = [
                create_report_header(file_path, total_pages, (actual_start, actual_end))
            ]
            
            total_images = 0
            analyzed_images = 0
            
            for page in self.processor.extract_pages(doc, actual_start, actual_end):
                image_analyses = []
                
                if page.images and analyze_images and self.config.gemini_api_key:
                    for img in page.images:
                        context = f"このページのテキスト: {page.text[:500]}..." if page.text else ""
                        analysis = await self.analyzer.analyze_image(img.data, context)
                        image_analyses.append(analysis)
                        analyzed_images += 1
                    total_images += len(page.images)
                elif page.images:
                    total_images += len(page.images)
                    image_analyses = ["*[画像解析スキップ: API Key未設定]*"] * len(page.images)
                
                page_md = page_to_markdown(page, image_analyses)
                markdown_parts.append(page_md)
            
            summary = create_summary_section(
                actual_end - actual_start + 1,
                total_images,
                analyzed_images
            )
            markdown_parts.insert(1, summary)
            
            doc.close()
            return "\n".join(markdown_parts)
            
        except Exception as e:
            return f"❌ エラー: {str(e)}"
    
    async def read_pdf_pages(
        self,
        file_path: str,
        pages: list[int],
        analyze_images: bool = True
    ) -> str:
        """指定ページのみ読み込み"""
        try:
            doc = self.processor.open(file_path)
            total_pages = self.processor.get_page_count(doc)
            
            markdown_parts = [
                create_report_header(file_path, total_pages),
                f"> 指定ページ: {', '.join(map(str, sorted(pages)))}\n\n---\n"
            ]
            
            for page in self.processor.extract_specific_pages(doc, pages):
                image_analyses = []
                
                if page.images and analyze_images and self.config.gemini_api_key:
                    for img in page.images:
                        context = f"このページのテキスト: {page.text[:500]}..." if page.text else ""
                        analysis = await self.analyzer.analyze_image(img.data, context)
                        image_analyses.append(analysis)
                
                page_md = page_to_markdown(page, image_analyses)
                markdown_parts.append(page_md)
            
            doc.close()
            return "\n".join(markdown_parts)
            
        except Exception as e:
            return f"❌ エラー: {str(e)}"
    
    def get_pdf_info(self, file_path: str) -> str:
        """PDF情報を取得"""
        try:
            doc = self.processor.open(file_path)
            metadata = doc.metadata
            
            lines = [
                "# PDF 情報",
                "",
                "| 項目 | 値 |",
                "|------|-----|",
                f"| ファイル名 | {Path(file_path).name} |",
                f"| 総ページ数 | {len(doc)} |",
            ]
            
            if metadata:
                if metadata.get("title"):
                    lines.append(f"| タイトル | {metadata['title']} |")
                if metadata.get("author"):
                    lines.append(f"| 作成者 | {metadata['author']} |")
            
            doc.close()
            return "\n".join(lines)
            
        except Exception as e:
            return f"❌ エラー: {str(e)}"
    
    def extract_text_only(
        self,
        file_path: str,
        start_page: int = 1,
        end_page: Optional[int] = None
    ) -> str:
        """テキストのみ抽出"""
        try:
            doc = self.processor.open(file_path)
            total_pages = self.processor.get_page_count(doc)
            actual_end = min(end_page, total_pages) if end_page else total_pages
            
            text_parts = []
            for page in self.processor.extract_pages(doc, start_page, actual_end):
                text_parts.append(f"--- ページ {page.page_num} ---\n")
                text_parts.append(page.text)
                text_parts.append("\n\n")
            
            doc.close()
            return "".join(text_parts)
            
        except Exception as e:
            return f"❌ エラー: {str(e)}"
    
    async def handle_tool_call(self, name: str, arguments: dict) -> str:
        """ツール呼び出しを処理"""
        if name == "read_pdf":
            return await self.read_pdf(
                file_path=arguments["file_path"],
                start_page=arguments.get("start_page", 1),
                end_page=arguments.get("end_page"),
                analyze_images=arguments.get("analyze_images", True)
            )
        elif name == "read_pdf_pages":
            return await self.read_pdf_pages(
                file_path=arguments["file_path"],
                pages=arguments["pages"],
                analyze_images=arguments.get("analyze_images", True)
            )
        elif name == "get_pdf_info":
            return self.get_pdf_info(arguments["file_path"])
        elif name == "extract_text_only":
            return self.extract_text_only(
                file_path=arguments["file_path"],
                start_page=arguments.get("start_page", 1),
                end_page=arguments.get("end_page")
            )
        else:
            return f"❌ 未知のツール: {name}"
    
    async def handle_request(self, request: dict) -> dict:
        """JSON-RPCリクエストを処理"""
        method = request.get("method", "")
        id_ = request.get("id")
        params = request.get("params", {})
        
        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": id_,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {
                        "name": "pdf-reader",
                        "version": "0.1.0"
                    }
                }
            }
        
        elif method == "tools/list":
            return {
                "jsonrpc": "2.0",
                "id": id_,
                "result": {"tools": self.get_tools()}
            }
        
        elif method == "tools/call":
            tool_name = params.get("name", "")
            arguments = params.get("arguments", {})
            result = await self.handle_tool_call(tool_name, arguments)
            return {
                "jsonrpc": "2.0",
                "id": id_,
                "result": {
                    "content": [{"type": "text", "text": result}]
                }
            }
        
        elif method == "notifications/initialized":
            # 通知は応答不要
            return None
        
        else:
            return {
                "jsonrpc": "2.0",
                "id": id_,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {method}"
                }
            }
    
    async def run_stdio(self):
        """標準入出力でMCPプロトコルを処理"""
        while True:
            try:
                line = await asyncio.get_event_loop().run_in_executor(
                    None, sys.stdin.readline
                )
                if not line:
                    break
                
                line = line.strip()
                if not line:
                    continue
                
                request = json.loads(line)
                response = await self.handle_request(request)
                
                if response:  # 通知の場合はNone
                    print(json.dumps(response), flush=True)
                    
            except json.JSONDecodeError as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {
                        "code": -32700,
                        "message": f"Parse error: {str(e)}"
                    }
                }
                print(json.dumps(error_response), flush=True)
            except Exception as e:
                sys.stderr.write(f"Error: {str(e)}\n")
                sys.stderr.flush()


def main():
    """サーバーを起動"""
    config = get_config()
    errors = config.validate()
    
    if errors:
        sys.stderr.write("⚠️ 設定警告:\n")
        for error in errors:
            sys.stderr.write(f"  - {error}\n")
        sys.stderr.write("画像解析機能は利用できませんが、テキスト抽出は可能です。\n")
        sys.stderr.flush()
    
    server = PDFReaderMCPServer()
    asyncio.run(server.run_stdio())


if __name__ == "__main__":
    main()
