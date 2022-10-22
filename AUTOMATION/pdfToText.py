import pdfminer.high_level

# Extract with Pdfminer.six Module
def With_PdfMiner():
	with open('test.pdf','rb') as fh:
		doc = pdfminer.high_level.extract_text(fh)
		print(doc)

if __name__ == '__main__':
	With_PdfMiner()
