'''
Source : https://github.com/iSiddharth20/DeepLearning-ImageClassification-Toolkit
'''

import matplotlib.pyplot as plt
import cv2
import numpy as np

'''
Helper Function 
    - Used to Show 2 Images Side-By-Side
'''
def images_on_side(img_1,label_1,img_2,label_2):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 24))
    ax1.imshow(img_1)
    ax1.set_title(label_1)
    ax2.imshow(img_2)
    ax2.set_title(label_2)
    plt.show()

'''
Helper Function 
    - Used to Extract Object from Image
'''
def image_processing(image_path):
    # Read the image
    img = cv2.imread(image_path)
    # Convert image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Threshold the image to get a binary mask
    _, thresholded = cv2.threshold(gray_img, 135, 255, cv2.THRESH_BINARY)
    # Perform morphological closing
    kernel_size = 5
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    closed_img = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)
    # Find contours
    contours, _ = cv2.findContours(closed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Identify the largest contour
    largest_contour = max(contours, key=cv2.contourArea)
    # Create an empty mask and draw the largest contour onto it
    contour_mask = np.zeros_like(thresholded)
    cv2.drawContours(contour_mask, [largest_contour], -1, (255), thickness=cv2.FILLED)
    # Dilate the mask slightly
    dilated_mask = cv2.dilate(contour_mask, kernel, iterations=1)
    # Use the mask to extract the largest object from the original image
    extracted_object = cv2.bitwise_and(img, img, mask=dilated_mask)
    return extracted_object
