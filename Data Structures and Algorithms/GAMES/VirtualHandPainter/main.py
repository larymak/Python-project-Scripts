import time

start = time.time()
from cv2 import VideoCapture, flip, COLOR_BGR2RGB, cvtColor, circle, FILLED, destroyAllWindows, imshow, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT
print("Importing cv stuff")
import mediapipe.python.solutions.drawing_utils as mp_drawing
print("Importing hand module  stuff")

import mediapipe.python.solutions.hands as mp_hands
print("Importing more hand module  stuff")

import pygame
print("Importing pygame")

from math import sqrt
print("Importing math")

import pyautogui
import os
print("Importing other stuff")


end = time.time()
print(end - start)

# 0.75s initial
# 0.73s final
# 3.5 x faster


# 640, 480
WIDTH, HEIGHT = 1000, 1000

# COLOURS
RED = (255, 0, 0)
VIOLET = (148, 0, 211)
INDIGO = (75, 0, 130)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 127, 0)
WHITE = (255, 255, 255)

color = RED
rainbow = [VIOLET, INDIGO, BLUE, GREEN, YELLOW, ORANGE, RED]

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
ss_count = 1

run = True

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Board")

hands = mp_hands.Hands(max_num_hands=1, min_tracking_confidence=0.9)
camera = VideoCapture(0)

camera.set(CAP_PROP_FRAME_WIDTH, WIDTH)
camera.set(CAP_PROP_FRAME_HEIGHT, HEIGHT)




def generate_rainbow(rainbow):
    it = iter(rainbow)
    while True:
        yield next(it)
        try:
            yield next(it)
        except StopIteration:
            it = iter(rainbow)


def convert_to_pixel_coordinates():
    normalized_landmark = handlms.landmark[id]
    pixel_coordinate = mp_drawing._normalized_to_pixel_coordinates(normalized_landmark.x,
                                                                   normalized_landmark.y, width, height)
    return pixel_coordinate


gen_rainbow = generate_rainbow(rainbow)
window.fill(WHITE)

while run:
    ret, frame = camera.read()
    frame = flip(frame, 1)
    imgRGB = cvtColor(frame, COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    hand = results.multi_hand_landmarks

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        run = False
    if keys[pygame.K_c]:
        window.fill(WHITE)
    if keys[pygame.K_r]:
        color = RED
    if keys[pygame.K_b]:
        color = BLUE
    if keys[pygame.K_y]:
        color = YELLOW
    if keys[pygame.K_g]:
        color = GREEN
    if keys[pygame.K_o]:
        color = ORANGE
    if keys[pygame.K_l]:
        color = next(gen_rainbow)

    if hand:
        for handlms in hand:
            for id, lm in enumerate(handlms.landmark):
                height, width, c = frame.shape
                cx, cy = int(lm.x * width), int(lm.y * height)

                if id == 4:
                    circle(frame, (cx, cy), 15, (255, 0, 0), FILLED)
                    thumb_coordinates = convert_to_pixel_coordinates()

                if id == 8:
                    circle(frame, (cx, cy), 15, (255, 0, 255), FILLED)
                    index_coordinates = convert_to_pixel_coordinates()

                    try:
                        x_distance = index_coordinates[0] - thumb_coordinates[0]
                        y_distance = index_coordinates[1] - thumb_coordinates[1]
                        distance = sqrt((x_distance ** 2) + (y_distance ** 2))

                        # try:
                        if 0 <= distance <= 20:
                            pygame.draw.circle(window, color,
                                               (index_coordinates[0], index_coordinates[1]), 5)
                    except TypeError:
                        print("ERROR")

                if id == 12:
                    circle(frame, (cx, cy), 15, (255, 255, 0), FILLED)
                    middle_tip_coordinates = convert_to_pixel_coordinates()

                    try:

                        x_middle_distance = index_coordinates[0] - middle_tip_coordinates[0]
                        y_middle_distance = index_coordinates[1] - middle_tip_coordinates[1]
                        distance_middle_to_index = distance = sqrt(
                            (x_middle_distance ** 2) + (y_middle_distance ** 2))

                        if 0 <= distance_middle_to_index <= 20:
                            print(desktop)
                            image = pyautogui.screenshot()
                            image.save(desktop + f"/screenshot{ss_count}.png")
                            ss_count += 1

                    except TypeError:
                        print("error")

                mp_drawing.draw_landmarks(frame, handlms, mp_hands.HAND_CONNECTIONS)

    pygame.display.update()
    imshow("Window", frame)

camera.release()
destroyAllWindows()
pygame.quit()
