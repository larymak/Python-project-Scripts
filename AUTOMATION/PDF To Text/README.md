# Extracting text from PDF using Python 

Create a new folder and create a pdfToText.py file in it. Copy and paste the code in pdfToText.py in this repository to that file.

Open the Terminal:

```py
    pip install pdfminer.six
```

In the same folder, add the pdf from which you want to extract text (Here the pdf used is test.pdf). Provide this pdf as a command line argument.

Run the script using:

```py
    python3 pdfToText.py test.pdf
```

The extracted text will be available in converted_pdf.txt