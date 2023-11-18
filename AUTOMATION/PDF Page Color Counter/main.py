from fastapi import FastAPI, UploadFile, File
import fitz
import cv2
from PIL import Image
import numpy as np
import os

app = FastAPI()

@app.post("/")
async def get_pdf(file : UploadFile = File(...)):
    #Initializing our variables.
    colored_page_count = 0
    color_list=[]
    black_list=[]
    num = 0
    black_count = 0
    #Getting the file name and then saving it in local.
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)
    # Open the PDF file
    # Get the full path to the uploaded file
    file_path = os.path.join(os.getcwd(), file.filename)
    print(file_path)
    with fitz.open(file_path) as doc:
        print(doc)
        # Iterate through the pages
        for _, page in enumerate(doc):
            # Render the page to an image
            pix = page.get_pixmap(alpha=False)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            

            arr = np.array(img)
            arr_mean = cv2.mean(arr)
            if not (arr_mean[0] == arr_mean[1] == arr_mean[2]):
                colored_page_count += 1
                num += 1
                color_list.append(num)
                #print('colored', num)
            else:
                num += 1
                black_count += 1
                black_list.append(num)
                #print('Black', num)
        print("\nColored Pages: ",color_list,"\n")
        print("Black & White Pages: ",black_list)
        #Close the file
    os.remove(file_path)    
    return {"colored : ":colored_page_count,"Black Count : ":black_count} 
