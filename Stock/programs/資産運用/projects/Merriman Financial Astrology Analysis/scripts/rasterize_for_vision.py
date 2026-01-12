import fitz  # PyMuPDF
import os
import sys
import datetime
import re

def rasterize_pdf(pdf_path, output_base_dir, dpi=300):
    """
    Converts each page of a PDF into a PNG image.
    Creates a subdirectory in output_base_dir based on the date found in filename or current date.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found at {pdf_path}")
        return

    # Extract date from filename (YYYY-MM-DD or similar) to organize folders
    base_name = os.path.basename(pdf_path)
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', base_name)
    
    if date_match:
        folder_date = date_match.group(1)
    else:
        # Fallback to today's date if not in filename
        folder_date = datetime.datetime.now().strftime('%Y-%m-%d')

    output_dir = os.path.join(output_base_dir, "images", folder_date)
    os.makedirs(output_dir, exist_ok=True)

    print(f"Opening PDF: {pdf_path}")
    doc = fitz.open(pdf_path)
    
    print(f"Rasterizing {len(doc)} pages to {output_dir} at {dpi} DPI...")
    
    generated_files = []
    
    for page_num, page in enumerate(doc):
        # Render page to pixmap
        pix = page.get_pixmap(dpi=dpi)
        
        # Construct image filename: page_01.png
        image_filename = f"page_{page_num+1:02d}.png"
        image_path = os.path.join(output_dir, image_filename)
        
        # Save image
        pix.save(image_path)
        generated_files.append(image_path)
        # print(f"Saved: {image_filename}") # Reduced verbosity

    print(f"Rasterization complete. {len(generated_files)} images saved.")
    return output_dir

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 rasterize_for_vision.py <pdf_path> [output_base_dir] [dpi]")
        # Default output dir logic relative to script location if not provided
        default_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../resources/weekly_reports"))
        print(f"Defaulting output to: {default_dir}")
        sys.exit(1)
        
    pdf_path = sys.argv[1]
    
    if len(sys.argv) > 2:
        output_base_dir = sys.argv[2]
    else:
        # determining project root relative to this script
        # script is in projects/Merriman.../scripts
        # resource is in projects/Merriman.../resources/weekly_reports
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_base_dir = os.path.normpath(os.path.join(script_dir, "../resources/weekly_reports"))

    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 300
    
    rasterize_pdf(pdf_path, output_base_dir, dpi)
