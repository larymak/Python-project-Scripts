# Analyze any `.docx` file for bold, underlined, italicized text
This program helps you find all the bold, underlined and italicized text in a word document.

First create a new folder and then create a file named `extract.py` inside it and copy paste the code to it.
Then you need to install `python-docx`
```bash
$ pip install python-docx
```
Copy your word document for example, `process_design_notes.docx` into the current working directory(CWD).

The CWD should now have two files i.e. **extract.py** and **process_design_notes.docx**.

Open a terminal or command prompt in CWD and type
```bash
#for linux
python3 extract.py process_design_notes.docx
#for windows
python extract.py process_design_notes.docx
```
After typing above command the program will execute on the word document and append the extracted bold, italicized, underlined words to it.
