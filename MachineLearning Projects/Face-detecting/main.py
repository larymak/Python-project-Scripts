# обнаруживает пока что только лицо и пишет на рамочке

import cv2

video = cv2.VideoCapture(0)
hands_hear_cascade = cv2.CascadeClassifier('Cascade-Files/more_bet.xml')

# Write some Text

font = cv2.FONT_ITALIC
text = 'Face detected'
fontScale = 1
fontColor = (0, 255, 0)
thickness = 3
lineType = 1

while True:
    _r, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hands = hands_hear_cascade.detectMultiScale(gray, 1.1, 3)

    if len(hands):
        print("Face")

        for x, y, w, h in hands:
            bottomLeftCornerOfText = (x - 5, y - 5)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, text,
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        thickness,
                        lineType)
    cv2.imshow("test", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
