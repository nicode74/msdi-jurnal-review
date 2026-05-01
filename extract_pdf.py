import pypdfium2 as pdfium
import pytesseract
import os

# Configure tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path, md_path):
    try:
        text = ""
        pdf = pdfium.PdfDocument(pdf_path)
        print(f"Loaded PDF with {len(pdf)} pages.")
        
        for i in range(len(pdf)):
            page = pdf[i]
            # render page to PIL Image
            bitmap = page.render(scale=2)  # scale 2 gives good resolution for OCR
            pil_image = bitmap.to_pil()
            
            # Extract text using Tesseract
            page_text = pytesseract.image_to_string(pil_image)
            text += f"\n--- Page {i+1} ---\n" + page_text + "\n"
            print(f"Extracted page {i+1}")
            
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(text)
            
        print(f"Successfully extracted text to {md_path}")
    except Exception as e:
        print(f"Error extracting text: {e}")

if __name__ == "__main__":
    extract_text_from_pdf("paper_original.pdf", "paper_converted.md")
