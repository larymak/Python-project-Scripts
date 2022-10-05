import cv2

img = cv2.imread('imaag.jpg')
height,width,channels= img.shape

left = img[:,:width//2]
right = img[:,width//2:]

cv2.imshow('original', img)
cv2.imshow('Left Half', left)
cv2.imshow('Right half', right)

cv2.imwrite('Left.jpg', left)
cv2.imwrite('Right.jpg', right)
cv2.waitKey(0)