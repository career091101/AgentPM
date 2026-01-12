#!/usr/bin/env python3
"""PDFをページごとに画像化するスクリプト"""

import fitz  # PyMuPDF
import os
import sys

def pdf_to_images(pdf_path, output_dir, start_page=1, end_page=None, dpi=150):
    """PDFの指定ページを画像として保存"""
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    
    if end_page is None or end_page > total_pages:
        end_page = total_pages
    
    # ファイル名のベース
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    for page_num in range(start_page - 1, end_page):
        page = doc[page_num]
        # 高解像度で描画
        mat = fitz.Matrix(dpi/72, dpi/72)
        pix = page.get_pixmap(matrix=mat)
        
        output_path = os.path.join(output_dir, f"{base_name}_p{page_num + 1:03d}.png")
        pix.save(output_path)
        print(f"Saved: {output_path}")
    
    doc.close()
    print(f"Done: {end_page - start_page + 1} pages saved")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pdf_to_images.py <pdf_path> <output_dir> [start_page] [end_page]")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_dir = sys.argv[2]
    start_page = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    end_page = int(sys.argv[4]) if len(sys.argv) > 4 else None
    
    pdf_to_images(pdf_path, output_dir, start_page, end_page)
