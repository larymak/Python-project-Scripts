import PyPDF2
import pyttsx3
from tkinter.filedialog import *

book = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.numPages

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()