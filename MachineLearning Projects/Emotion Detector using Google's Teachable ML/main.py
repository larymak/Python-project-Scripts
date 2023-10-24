import cv2
import numpy as np
import mediapipe as mp
from keras.models import  load_model
from keras.preprocessing import image
# from tensorflow.keras.utils import img_to_array
from PIL import Image, ImageOps

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

model = load_model('./Teachable ML Data/keras_model.h5')

cap = cv2.VideoCapture(1)

results_detect = {0:"😁",1:"😠",2:"☹️",3:"😊",4:"😲"}
results_detect_str = {0:"happy",1:"angry",2:"sad",3:"smile",4:"surprise"}

# pTime = 0
while cap.isOpened():
    _,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    if results.detections:
        ih,iw,ic = img.shape
        for id,detection in enumerate(results.detections):
            bBoxC = detection.location_data.relative_bounding_box
            bBox = int(bBoxC.xmin * iw),int(bBoxC.ymin * ih),int(bBoxC.width * iw),int(bBoxC.height * ih)
            # cv2.rectangle(img,bBox,(255,0,255),2)
            roi_gray = img[bBox[1]:bBox[1] + bBox[2], bBox[0]:bBox[0] + bBox[3]]
            roi_gray = cv2.resize(roi_gray, (224, 224))
            cv2.imwrite("image.jpg",roi_gray)


            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            image = Image.open('image.jpg')
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.ANTIALIAS)
            image_array = np.asarray(image)
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
            data[0] = normalized_image_array
            prediction = model.predict(data)
            res = np.argmax(prediction)

            # predictions = np.argmax(model.predict(np.array([roi_gray])))
            # cv2.putText(img, results_detect[res], (150,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            temp_emotion = cv2.imread(f"./emotions/{results_detect_str[res]}.jfif")
            cv2.imshow("emotion", temp_emotion)
            print(results_detect[res])

    cv2.imshow("Image",img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break