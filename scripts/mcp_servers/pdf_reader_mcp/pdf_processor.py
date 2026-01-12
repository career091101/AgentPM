"""PDF処理モジュール - PyMuPDFを使用"""

import io
import tempfile
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, Iterator, AsyncIterator
import fitz  # PyMuPDF
from PIL import Image


@dataclass
class ExtractedImage:
    """抽出された画像"""
    index: int
    page_num: int
    data: bytes
    width: int
    height: int
    format: str = "png"
    
    def save(self, path: Path) -> Path:
        """画像をファイルに保存"""
        output_path = path / f"page{self.page_num}_img{self.index}.{self.format}"
        output_path.write_bytes(self.data)
        return output_path


@dataclass
class PageContent:
    """ページのコンテンツ"""
    page_num: int
    text: str
    images: list[ExtractedImage]


class PDFProcessor:
    """PDF処理クラス"""
    
    def __init__(self, min_image_size: int = 100):
        """
        Args:
            min_image_size: 抽出する画像の最小サイズ（幅または高さ）
        """
        self.min_image_size = min_image_size
    
    def open(self, file_path: str) -> fitz.Document:
        """PDFファイルを開く"""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"PDFファイルが見つかりません: {file_path}")
        if not path.suffix.lower() == ".pdf":
            raise ValueError(f"PDFファイルではありません: {file_path}")
        
        return fitz.open(file_path)
    
    def get_page_count(self, doc: fitz.Document) -> int:
        """総ページ数を取得"""
        return len(doc)
    
    def extract_page(self, doc: fitz.Document, page_num: int) -> PageContent:
        """
        単一ページからテキストと画像を抽出
        
        Args:
            doc: PDFドキュメント
            page_num: ページ番号（0から始まる）
        """
        if page_num < 0 or page_num >= len(doc):
            raise ValueError(f"無効なページ番号: {page_num} (総ページ数: {len(doc)})")
        
        page = doc[page_num]
        
        # テキスト抽出（レイアウト保持モード）
        text = page.get_text("text")
        
        # 画像抽出
        images = self._extract_images_from_page(page, page_num)
        
        return PageContent(
            page_num=page_num + 1,  # 1から始まるページ番号に変換
            text=text.strip(),
            images=images
        )
    
    def _extract_images_from_page(self, page: fitz.Page, page_num: int) -> list[ExtractedImage]:
        """ページから画像を抽出"""
        images = []
        image_list = page.get_images(full=True)
        
        for img_index, img_info in enumerate(image_list):
            try:
                xref = img_info[0]
                base_image = page.parent.extract_image(xref)
                
                if base_image is None:
                    continue
                
                image_bytes = base_image["image"]
                width = base_image["width"]
                height = base_image["height"]
                
                # 小さすぎる画像はスキップ
                if width < self.min_image_size or height < self.min_image_size:
                    continue
                
                # PNG形式に変換
                img = Image.open(io.BytesIO(image_bytes))
                png_buffer = io.BytesIO()
                img.save(png_buffer, format="PNG")
                png_bytes = png_buffer.getvalue()
                
                images.append(ExtractedImage(
                    index=img_index + 1,
                    page_num=page_num + 1,
                    data=png_bytes,
                    width=width,
                    height=height,
                    format="png"
                ))
            except Exception:
                # 画像抽出に失敗した場合はスキップ
                continue
        
        return images
    
    def extract_pages(
        self,
        doc: fitz.Document,
        start_page: int = 1,
        end_page: Optional[int] = None
    ) -> Iterator[PageContent]:
        """
        複数ページを順次抽出（ジェネレータ）
        
        Args:
            doc: PDFドキュメント
            start_page: 開始ページ（1から始まる）
            end_page: 終了ページ（1から始まる、Noneで最終ページまで）
        """
        total_pages = len(doc)
        
        # ページ番号の検証と調整
        start_idx = max(0, start_page - 1)
        end_idx = min(total_pages, end_page) if end_page else total_pages
        
        for page_num in range(start_idx, end_idx):
            yield self.extract_page(doc, page_num)
    
    def extract_specific_pages(
        self,
        doc: fitz.Document,
        pages: list[int]
    ) -> Iterator[PageContent]:
        """
        指定した特定のページのみを抽出
        
        Args:
            doc: PDFドキュメント
            pages: ページ番号のリスト（1から始まる）
        """
        total_pages = len(doc)
        
        for page_num in pages:
            if 1 <= page_num <= total_pages:
                yield self.extract_page(doc, page_num - 1)
