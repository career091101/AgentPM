import fitz  # PyMuPDF
import os
import sys

def rasterize_pdf(pdf_path, output_dir, dpi=200):
    """
    Converts each page of a PDF into a PNG image.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found at {pdf_path}")
        return

    doc = fitz.open(pdf_path)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Create images directory (separate from extracting embedded images)
    pages_dir = os.path.join(output_dir, "page_images")
    os.makedirs(pages_dir, exist_ok=True)
    
    print(f"Rasterizing {len(doc)} pages from {base_name} at {dpi} DPI...")
    
    for page_num, page in enumerate(doc):
        # Render page to pixmap
        pix = page.get_pixmap(dpi=dpi)
        
        # Construct image filename
        # page_01.png for easy sorting
        image_filename = f"page_{page_num+1:02d}.png"
        image_path = os.path.join(pages_dir, image_filename)
        
        # Save image
        pix.save(image_path)
        print(f"Saved: {image_path}")

    print(f"Rasterization complete. Images saved to: {pages_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 rasterize_pdf.py <pdf_path> [output_dir] [dpi]")
        sys.exit(1)
        
    pdf_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(pdf_path)
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    
    rasterize_pdf(pdf_path, output_dir, dpi)
