import fitz  

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Extract text from each page
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    
    return text

if __name__ == "__main__":
    pdf_path = r"E:\study\btech\New Projects\Ml\Pdf-text Extraction\kech101.pdf"  
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)
