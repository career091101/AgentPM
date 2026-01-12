"""Markdown生成ユーティリティ"""

from typing import Optional
from .pdf_processor import PageContent


def page_to_markdown(
    page: PageContent,
    image_analyses: Optional[list[str]] = None
) -> str:
    """
    ページコンテンツをMarkdown形式に変換
    
    Args:
        page: ページコンテンツ
        image_analyses: 画像解析結果のリスト（画像と同じ順序）
    """
    lines = [f"## ページ {page.page_num}", ""]
    
    # テキストセクション
    if page.text:
        lines.append("### テキスト内容")
        lines.append("")
        lines.append(page.text)
        lines.append("")
    
    # 画像セクション
    if page.images:
        lines.append("### 画像分析")
        lines.append("")
        
        for i, img in enumerate(page.images):
            lines.append(f"#### 画像 {img.index} ({img.width}x{img.height})")
            lines.append("")
            
            if image_analyses and i < len(image_analyses):
                lines.append(image_analyses[i])
            else:
                lines.append("*[画像解析待ち]*")
            
            lines.append("")
    
    return "\n".join(lines)


def create_report_header(
    file_path: str,
    total_pages: int,
    processed_pages: Optional[tuple[int, int]] = None
) -> str:
    """
    レポートのヘッダーを生成
    
    Args:
        file_path: PDFファイルパス
        total_pages: 総ページ数
        processed_pages: 処理したページ範囲 (start, end)
    """
    from pathlib import Path
    from datetime import datetime
    
    filename = Path(file_path).name
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    lines = [
        "# PDF レポート分析結果",
        "",
        "| 項目 | 値 |",
        "|------|-----|",
        f"| ファイル名 | {filename} |",
        f"| 総ページ数 | {total_pages} |",
    ]
    
    if processed_pages:
        lines.append(f"| 処理範囲 | {processed_pages[0]} - {processed_pages[1]} ページ |")
    
    lines.extend([
        f"| 生成日時 | {now} |",
        "",
        "---",
        "",
    ])
    
    return "\n".join(lines)


def create_summary_section(
    total_pages: int,
    total_images: int,
    analyzed_images: int
) -> str:
    """サマリーセクションを生成"""
    lines = [
        "## 📊 処理サマリー",
        "",
        f"- 処理ページ数: **{total_pages}**",
        f"- 抽出画像数: **{total_images}**",
        f"- 解析済み画像: **{analyzed_images}**",
        "",
        "---",
        "",
    ]
    return "\n".join(lines)
