import argparse
import pdfminer.high_level

# Extract text with Pdfminer.six Module
def With_PdfMiner(pdf):
	with open(pdf,'rb') as file_handle:
		doc = pdfminer.high_level.extract_text(file_handle)
		print(doc)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help = "PDF file from which we extract text")
	args = parser.parse_args()
	# print()
	With_PdfMiner(args.file)
