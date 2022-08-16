from concurrent.futures import process
from distutils.cmd import Command
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import os

root=Tk()
root.title("Python IDE")
root.geometry("1280x720+150+80")
root.configure(bg="black")
root.resizable(True,False)

file_path = ''

def set_file_path(path):
    global file_path
    file_path=path

def open_file():
    path = askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path, 'r') as file:
        code = file.read()
        srccode.delete('1.0', END)
        srccode.insert('1.0', code)
        set_file_path(path)

def save():
    if file_path=='':
        path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path=file_path

    with open(path, 'w') as file:
        code= srccode.get('1.0', END)
        file.write(code)
        set_file_path(path)

def run():
    if file_path == '':
        messagebox.showerror("Python Ide","Warning Save Code")
        return
    Command = f'python {file_path}'
    process = subprocess.Popen(Command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
    result , error = process.communicate()
    output.insert('1.0', result)
    output.insert('1.0',error)


#icon
#logo=PhotoImage(file="logo.png")
#root.iconphoto(False, logo)

#code input pane
srccode = Text(root,font="cosolas 18")
srccode.place(x=160,y=0,width=680,height=720)

#code output pane
output = Text(root, font="cosolas 12",bg="black", fg="lightgreen")
output.place(x=860,y=0,width=420,height=720)

#button
Open=PhotoImage(file="C:/Users/Shivam/AppDev/PCE/open.png")
Save=PhotoImage(file="C:/Users/Shivam/AppDev/PCE/Save.png")
Run=PhotoImage(file="C:/Users/Shivam/AppDev/PCE/run.png")

Button(root, image=Open,bg="#323846",bd=0,command=open_file).place(x=30,y=30)
Button(root, image=Save,bg="#323846",bd=0,command=save).place(x=30,y=130)
Button(root, image=Run,bg="#323846",bd=0,command=run).place(x=30,y=230)

root.mainloop()


