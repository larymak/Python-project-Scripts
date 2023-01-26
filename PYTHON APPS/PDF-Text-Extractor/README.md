# PDF-Text-Extractor
This GUI Application allows you to extract the texgt from the PDF files. The project is build using the PyPDF2 library for extracting text from PDFs, and the tkinter library for creating the GUI.

## Getting Started
To run the project, you will need to have Python and pip installed on your system.

### Installation
1. Clone or download the repository to your local machine.

   ```
   git clone https://github.com/SamAddy/PDF-Extract-Text.git
   ```

2. Enter the working directory.

   ```
   cd PDF-Extract-Text
   ```

3. Use pip to install the required libraries.

   ```
   pip install -r requirements.txt
   ```

### Usage
1. Run the app using the following command:

   ```
   python app.py
   ```

2. A GUI window will appear, with a button to selecgt the PDF file you want to extract text from. 

3. Once you have selected the file, the text will be extracted and displayed in the text box. 

4. You can also save the text to a file by clicking 'Save' button.

<!--
<p align="center">
<img src="https://github.com/SamAddy/PDF-Extract-Text/blob/main/Stage1.png" width=50% alt="Browse file"/>
<img src="https://github.com/SamAddy/PDF-Extract-Text/blob/main/Stage2.png" width=50% alt="Display extractedtext">
</p>


<p align="center">
![Browse file](https://github.com/SamAddy/PDF-Extract-Text/blob/main/Stage1.png)
![Diplay text in textbox](https://github.com/SamAddy/PDF-Extract-Text/blob/main/Stage2.png)
</p>
-->

<table align="center">
  <tr>
    <td>
      <img src="https://github.com/SamAddy/PDF-Extract-Text/blob/main/Stage1.png" alt="image1" width="400"/>
    </td>
    <td>
      <img src="https://github.com/SamAddy/PDF-Extract-Text/blob/main/Stage2.png" alt="image2" width="400"/>
    </td>
  </tr>
</table>



### Note 
Please keep in mind that not all pdfs are created equal, and some pdfs may have text in an image format or other format that may not be extractable with PyPDF2.

### Built With
 * [Python](https://www.python.org/) - The programming language used.
 * [PYPDF2](https://pypi.org/project/PyPDF2/) - A library for extracting text from PDF files.
 * [Tkinter](https://docs.python.org/3/library/tk.html) - A library for creating GUI in Python.

### Contributing 
Contributions are absolutely welcome. If you have an idea for an improvement, please open an issue or submit a pull request.

### Acknowledgement
* Inspiration [Mariya Sha](https://github.com/MariyaSha/PDFextract_text)
