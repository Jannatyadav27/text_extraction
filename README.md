# Python Script for Extracting Text from PDF
####  This Python script is designed to extract text from a PDF file using the PyMuPDF library. The script processes each page of the PDF and extracts the text content, which can then be used for various text processing tasks.

## Key Features:
1. PDF Text Extraction: The script reads a PDF file and extracts text from each page.

2. Simple and Efficient: It leverages the PyMuPDF library, which is known for its speed and efficiency in handling PDFs.

3. Easy to Use: Just provide the path to your PDF file, and the script will output the extracted text.
## How It Works:
1. Open PDF File: The script opens the PDF file using the fitz.open() function from the PyMuPDF library.

2. Extract Text: It iterates over each page in the PDF, extracting the text content using page.get_text().

3. Combine Text: The extracted text from all pages is combined into a single string.

4. Output: The script prints the combined text, which can be redirected to a file or processed further.

## Usage:
1. Install the required library: pip install pymupdf.

2. Replace "E:\study\btech\New Projects\Ml\Pdf-text Extraction\kech101.pdf" in the script with the path to your PDF file.

3. Run the script to extract and print the text from the PDF.
