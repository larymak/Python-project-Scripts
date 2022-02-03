import os
import winsound

import cv2
import face_recognition
import numpy


class FaceRecognition:

    def __init__(self):
        self.images = []
        self.base_names = []
        self.encoded_faces = []
        self.path = 'images'
        print('please wait my dummy program is busy encoding...')
        self.camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.known_encoded_faces = []
        self.frame_one = None
        self.video_capture = None

    def save_video_stream(self):
        os.makedirs('Security Camera Video', exist_ok=True)
        name = 'Video1.avi'
        if name in os.listdir('Security Camera Video'):
            name = f'{os.path.splitext(name)[0][:-1]}' \
                   f'{len(os.listdir("Security Camera Video")) + 1}' \
                   f'{os.path.splitext(name)[1]}'
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.video_capture = cv2.VideoWriter(os.path.join('Security Camera Video', name),
                                             fourcc, 20.0, (640, 480))
        print(f'{name} saving ...')

    def known_image_folder(self):
        for image in os.listdir(path=self.path):
            if not (image.endswith('.jpeg') or image.endswith('.JPG')
                    or image.endswith('.jpg') or image.endswith(
                    '.png') or image.endswith('.PNG')):
                continue
            img = cv2.imread(f"{self.path}/{image}")
            self.images += [img]
            self.base_names += [os.path.splitext(image)[0]]

    def encode_face(self, images):
        for image in images:
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            face_encoding = face_recognition.face_encodings(image_rgb)[0]
            self.encoded_faces += [face_encoding]
        return self.encoded_faces

    def run(self):
        self.known_image_folder()
        self.known_encoded_faces = self.encode_face(self.images)
        print("Encoding Complete, camera opening...")
        self.save_video_stream()
        self.open_camera_tasks()

    def open_camera_tasks(self):
        while self.camera.isOpened():
            _, self.frame_one = self.camera.read()
            self.detect_faces()
            self.video_capture.write(self.frame_one)
            cv2.imshow("Press 'c' to capture image, q to quit.", self.frame_one)
            key = cv2.cv2.waitKey(1)
            if key == ord('q') or key == 27:
                self.exit_protocol()
            elif key == ord('c') or key == 32:
                self.save_image_capture()

    def save_image_capture(self):
        os.makedirs('Security Camera Images', exist_ok=True)
        name = 'Image1.png'
        if name in os.listdir('Security Camera Images'):
            name = f"{os.path.splitext(name)[0][:-1]}\
            {len(os.listdir('Security Camera Images')) + 1}" \
                   f"{os.path.splitext(name)[1]}"
        cv2.imwrite(os.path.join('Security Camera Images', name), self.frame_one)
        print(f"{name} captured successfully.")

    def detect_faces(self):
        frame_one_rgb = cv2.cvtColor(self.frame_one, cv2.COLOR_BGR2RGB)
        face_location = face_recognition.face_locations(frame_one_rgb)
        face_encoding = face_recognition.face_encodings(frame_one_rgb, face_location)
        for face_encoded, face_located in zip(face_encoding, face_location):
            self.face_comparison(face_encoded, face_located)

    def face_comparison(self, face_encoded, face_located):
        compare_face = face_recognition.compare_faces(self.known_encoded_faces, face_encoded)
        face_distance = face_recognition.face_distance(self.known_encoded_faces, face_encoded)
        distance_index = numpy.argmin(face_distance)
        if compare_face[distance_index]:
            name = self.base_names[int(distance_index)].title()
            x, y, w, h = face_located
            cv2.rectangle(self.frame_one, (h, x), (y, w), (0, 255, 0), 2)
            cv2.rectangle(self.frame_one, (h, x-40), (y, w), (0, 255, 0), 2)
            cv2.putText(self.frame_one, name, (
                h + 30, x - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 255), 2)
        else:
            x, y, w, h = face_located
            cv2.rectangle(self.frame_one, (h, x), (y, w), (0, 255, 0), 2)
            cv2.rectangle(self.frame_one, (h, x - 40), (y, w), (0, 255, 0), 2)
            cv2.putText(self.frame_one, "Unknown", (h, x - 10),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 255),
                        2)
            winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
            print("Intruder in the house.")

    def exit_protocol(self):
        self.camera.release()
        self.video_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    FaceRecognition().run()
