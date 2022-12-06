from tkinter import *
from PIL import ImageTk, Image
from textblob import TextBlob

root = Tk()
root.title("Spelling Corrector")
root.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\bee_icon_177139.ico")
root.geometry('500x500')

img = ImageTk.PhotoImage(Image.open(r"C:\Users\FUTURE LAPTOP\Downloads\Spelling Corrector.png"))
label = Label(root, image=img)
label.place(relx=0.5, rely=0.12, anchor=CENTER)

img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\FUTURE LAPTOP\Downloads\Untitled design.png"))
label2 = Label(root, image=img2)
label2.place(relx=0.58, rely=0.82, anchor=W)

my_frame = LabelFrame(root, text="Correct Spellings", font=("Roboto", 15), fg="#000000", padx=100, pady=10)
my_frame.pack(padx=15, pady=150)

Label(my_frame, text="Your Word: ", font=("Roboto", 15), padx=7, relief="groove").\
    grid(row=0, column=0, columnspan=2, padx=2, pady=5, sticky="W")

enter_word = Entry(my_frame, highlightthickness=2)
enter_word.config(highlightbackground="#FFFF00", highlightcolor="#FFFF00")
enter_word.grid(row=0, column=2, padx=2, pady=5, sticky="W")


# Parsing the given string into individual characters.
def parse_string(string):
    charc_list = list(string.split())
    return charc_list


def clicked(word):
    word_charc = parse_string(word)

    correct_word_charc = []
    corrected = ""

    for i in word_charc:
        correct_word_charc.append(TextBlob(i))

    for i in correct_word_charc:
        corrected = i.correct()

    Label(my_frame, text="Correct Word: ", font=("Roboto", 15), padx=7, relief="groove"). \
        grid(row=2, column=0, columnspan=2, padx=2, pady=5, sticky="W")

    Label(my_frame, text=corrected, font=("Roboto", 15), padx=7, relief="groove"). \
        grid(row=2, column=2, padx=2, pady=5, sticky="W")


my_button = Button(my_frame, text="Enter", font=("Roboto", 13), width=7, padx=2, bg="#FFFF00", fg="#000000",
                   command=lambda: clicked(enter_word.get()))
my_button.grid(row=1, column=0, columnspan=2, padx=4, pady=5, sticky="W")

root.mainloop()
