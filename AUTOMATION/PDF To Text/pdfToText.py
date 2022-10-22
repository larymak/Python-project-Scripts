import argparse
import pdfminer.high_level

# Extract text with Pdfminer.six Module
def With_PdfMiner(pdf):
	with open(pdf,'rb') as file_handle_1:
		doc = pdfminer.high_level.extract_text(file_handle_1)

	with open('converted_pdf.txt','w') as file_handle_2 :
		file_handle_2.write(doc)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help = "PDF file from which we extract text")
	args = parser.parse_args()
	With_PdfMiner(args.file)
