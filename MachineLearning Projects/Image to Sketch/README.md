# Image to Pencil Sketch using python

👉 The mission here is to convert the Image into pencil sketch.

![dog](https://user-images.githubusercontent.com/82924828/191065579-f0f29b4f-dda3-44f1-985d-042e11086e49.jpg)

👉 First, convert the RGB image into grayscale.

![download](https://user-images.githubusercontent.com/82924828/191065626-8caf751d-5480-452a-81a5-78d6cd21ab5f.png)

👉 Then convert the grayscale into negative imaging which is inverting the grayscale image.

![dog_sketch](https://user-images.githubusercontent.com/82924828/191066033-04489ba7-1c13-4f0d-ae7c-60e82c12f2a7.jpg)

👉 This can be done by dividing the grayscale image by the inverted blurry image.


![dog_sketch2](https://user-images.githubusercontent.com/82924828/191066150-a770a274-546a-47eb-ad4b-24fdcdd8fdfe.jpg)

👉 These things can be done using cv2 library.
