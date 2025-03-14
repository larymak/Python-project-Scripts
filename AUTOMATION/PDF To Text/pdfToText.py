from pathlib import Path
from PyPDF2 import PdfReader


def convert_pdf(filename):
    my_file = Path(filename)
    
    # Check if provided PDF file exists
    if not my_file.is_file():
        print('Error! File Not Found!')
        return None
    print('PDF Found! Attempting Conversion...')
    
    # Exception Handling during Data Extraction from PDF File
    try:
        # Define .txt file which will contain the extracted data 
        out_filename = my_file.with_suffix('.txt')
        # Extracting Data from PDF file page-by-page and storing in TXT file
        pdf_reader = PdfReader(filename)
        with open(out_filename, 'w', encoding='utf-8') as extracted_data:
            for page in pdf_reader.pages:
                text = page.extract_text()
                extracted_data.write(text)
        print('PDF to TXT Conversion Successful!')
        
    # If any Error is encountered, Print the Error on Screen
    except Exception as e:
        print(f'Error: {e}')
        if out_filename.exists():
            out_filename.unlink()
        return None


if __name__ == '__main__':
    file = input('Enter Full Path and FileName: ')
    convert_pdf(file)
