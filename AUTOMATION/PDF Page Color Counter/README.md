<!--Please do not remove this part-->
![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# PDF Page Color Counter

## 🛠️ Description
This Python project provides a simple yet powerful tool for analyzing PDF documents and counting the number of black and color pages. Whether you're working on document analysis, quality control, or just curious about the composition of your PDF files, this code helps you gain insights into the document's visual characteristics.

**Key Features:**

* Easy Integration: With a few lines of code, you can integrate this functionality into your Python applications or workflows.

* PDF Expertise: Utilizing the PyMuPDF (MuPDF) library, this project efficiently processes PDF files, making it suitable for a wide range of applications.

* Color Page Detection: It accurately identifies color and black & white pages within the PDF document, providing valuable statistics.

* Use Cases: This code can be employed in various scenarios, such as document archiving, printing optimization, or content analysis.

## ⚙️ Languages or Frameworks Used
- **Python**: The primary programming language used for the project.
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **PyMuPDF (MuPDF)**: A lightweight and efficient PDF processing library for Python.
- **OpenCV**: Used for image analysis and processing.
- **Pillow (PIL)**: Python Imaging Library for working with images.

## 🌟 How to run
 - ### Install all the requirements
    Run `pip install -r requirements.txt` to install all the requirements.
 - ### Setup a Virtual Enviroment

   - Run this command in your terminal `python -m venv myenv`.
   - Change your directory by `cd myenv/Scripts` if on windows.
   - Activate the virtual enviroment by running this command `source activate`.
   - Move out from virtual env to your **Project Directory** by `cd..` .
   - Install the packages if not present - `uvicorn`, `fastapi`, `fitz`, `frontend`, `tools`, `opencv-python`, `pillow`, `python-multipart`, `PyMuPDF`.
   ```
   pip install uvicorn fastapi fitz frontend tools opencv-python pillow python-multipart PyMuPDF
   ```

- ###  Now Just, Run the project
   
   -Now Run the following command - `uvicorn main:app --reload`.
   -Open the localhost link on your browser and put `/docs` at your endpoint to see the fastapi docs UI.
   ![Screenshot 2023-10-25 134746](https://github.com/Om25091210/Count-Color-Black-Pages-PDF/assets/74484315/2b5b64a2-1c00-4a5a-ab7c-99fb30e7aba6)

   -Now, Click on **POST** and then **Try it out**.
   -Click on **Choose file** to select a pdf, which you want to count the number of black and color pages.
   -Click on **Execute**.


## 📺 Demo
![Screenshot 2023-10-25 133406](https://github.com/Om25091210/Count-Color-Black-Pages-PDF/assets/74484315/a84def7c-7db4-4ab5-bf0b-f8cfe5ded66b)


## 🤖 Author

Github - [OM YADAV](https://github.com/Om25091210)
LinkedIn - [OM YADAV](www.linkedin.com/in/omyadav)




