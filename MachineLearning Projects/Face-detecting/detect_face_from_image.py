import cv2

img = cv2.imread('images/im1.jpg')
img2 = cv2.imread('images/im2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

window_name = 'Image'

faces = cv2.CascadeClassifier('Cascade-Files/more_bet.xml')

results = faces.detectMultiScale(gray, 1.1, 4)
# results = faces.detectMultiScale(gray2, 1.1, 4)

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow(window_name, img)
cv2.waitKey(0)
