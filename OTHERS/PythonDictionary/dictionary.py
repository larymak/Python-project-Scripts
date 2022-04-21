from tkinter import *
from PyDictionary import PyDictionary

# Create a window
dictionary = PyDictionary()
root = Tk()

# set geometry
root.title("Dictionary")
root.geometry("600x400+50+50")


def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))


# Add labels, buttons and frame
Label(root, text="My Dictionary", font=(
    "Poppins, 20 bold"), fg="Orange").pack(pady=20)

# Frame 1
frame = Frame(root)
Label(frame, text="Enter word: ", font=(
    "Helvetica, 15 bold")).pack(side="left")
word = Entry(frame, font=("Helvetica, 15 bold"), width=30)
word.pack()
frame.pack(pady=10)

# Frame 2
frame1 = Frame(root)
Label(frame1, text="Meaning: ", font=("Aerial, 15 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Poppins, 15"))
meaning.pack()
frame1.pack(pady=10)

# Frame 3
frame2 = Frame(root)
Label(frame2, text="Synonym: ", font=(
    "Roboto, 15 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Roboto, 15"))
synonym.pack()
frame2.pack(pady=10)

# Frame 4
frame3 = Frame(root)
Label(frame3, text="Antonym: ", font=("Helvetica, 15 bold")).pack(side=LEFT)
antonym = Label(frame3, text="", font=("Helvetica, 15"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)

Button(root, text="Search", font=("Helvetica, 15 bold"), command=dict).pack()

# Execute Tkinter
root.mainloop()
