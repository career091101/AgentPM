import fitz  # PyMuPDF
import os
import sys

def extract_content(pdf_path, output_dir):
    """
    Extracts text and images from a PDF file.
    Images are saved as PNG files in an 'images' subdirectory.
    Text is saved with [IMAGE: path] placeholders.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found at {pdf_path}")
        return

    doc = fitz.open(pdf_path)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Create images directory
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    
    full_text = ""
    
    # Text Extraction using pypdf as primary/fallback (since fitz failed on zlib)
    try:
        import pypdf
        reader = pypdf.PdfReader(pdf_path)
        print(f"pypdf: Found {len(reader.pages)} pages.")
    except Exception as e:
        print(f"pypdf import/init failed: {e}")
        reader = None

    full_text = ""
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Try pypdf for text first
        page_text = ""
        if reader and page_num < len(reader.pages):
            try:
                page_text = reader.pages[page_num].extract_text()
            except Exception as e:
                print(f"pypdf extraction failed on page {page_num}: {e}")
        
        # Fallback to fitz if pypdf empty (though fitz failed before)
        if not page_text.strip():
             page_text = page.get_text()

        # Extract Images (fitz)
        image_list = page.get_images(full=True)
        page_content = f"\n--- Page {page_num + 1} ---\n"
        
        page_content += page_text + "\n"
        
        for img_index, img in enumerate(image_list):
            xref = img[0]
            try:
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                
                # Construct image filename
                image_filename = f"{base_name}_page{page_num+1}_img{img_index+1}.{image_ext}"
                image_path = os.path.join(images_dir, image_filename)
                
                # Save image
                with open(image_path, "wb") as f:
                    f.write(image_bytes)
                
                # Append placeholder to text
                page_content += f"\n[IMAGE: {image_path}]\n"
            except Exception as e:
                print(f"Image extraction failed on page {page_num} image {img_index}: {e}")
            
        full_text += page_content

    # Save full text
    text_output_path = os.path.join(output_dir, f"{base_name}_extracted.txt")
    with open(text_output_path, "w", encoding="utf-8") as f:
        f.write(full_text)
        
    print(f"Extraction complete.")
    print(f"Text saved to: {text_output_path}")
    print(f"Images saved to: {images_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 extract_report_content.py <pdf_path> [output_dir]")
        sys.exit(1)
        
    pdf_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(pdf_path)
    
    extract_content(pdf_path, output_dir)
