from PyPDF2 import PdfFileMerger

# array of PDFs which need to merge 
pdfs = ['repo.pdf', 'python.pdf']

merger = PdfFileMerger(strict=False)

for pdf in pdfs:
    merger.append(pdf)

merger.write("Merged_result.pdf")
print('PDF Merged Wohh !!')
merger.close()