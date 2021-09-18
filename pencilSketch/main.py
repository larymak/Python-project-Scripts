import cv2

#reading image
image = cv2.imread("res/girl3.jpg")

#converting BGR image to grayscale
#cvtColor -> https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#image invert
inverted_image = 255 - gray_image

#blurring image
#GaussianBlur -> https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1
blurred_image = cv2.GaussianBlur(gray_image, (43, 43), 0)
pencil_sketch = cv2.divide(gray_image, blurred_image, scale=250.0)

cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)