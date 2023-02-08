import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
root.title('PDF to TEXT')
root.iconbitmap('./logo.png')
root.resizable(False, False)


canvas = tk.Canvas(root, width=600, height=400)
canvas.grid(columnspan=3, rowspan=3)

# Insert logo into the window
logo = Image.open('logo2.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = tk.Label(root, text='Select a PDF file on your device to extract all its text.', font='calibre')
instructions.grid(columnspan=3, column=0, row=1)

# Get the PDF file on device
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), font='calibre', bg='red', width=15, height=2)
browse_text.set('Browse')
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=200)
canvas.grid(columnspan=3, rowspan=3)


def open_file():
    browse_text.set('On it...')
    # Open the PDF file using the PdfFileReader object
    file = askopenfile(parent=root, mode='rb', title='Choose a file', filetypes=[('PDF file', '*.pdf')])
    text = ""

    if file:
        read_pdf = PyPDF2.PdfReader(file)
        for i in range(len(read_pdf.pages)):
            text += read_pdf.pages[i].extract_text()

        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, text)
        text_box.tag_config('center', justify='center')
        text_box.tag_add('center', 1.0, 'end')
        text_box.grid(column=1, row=3)

        browse_text.set('Browse')


def convert_to_docx():
    pass


root.mainloop()
