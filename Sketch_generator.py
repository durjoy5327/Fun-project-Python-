import cv2
import turtle
import numpy as np
from matplotlib import pyplot as plt
import time
import os

def find_closest(p, positions):
    if len(positions) > 0:
        nodes = np.array(positions)
        distances = np.sum((nodes - p) ** 2, axis=1)
        i_min = np.argmin(distances)
        return positions[i_min]
    else:
        return None

def outline(image):
    src_image = cv2.imread(image, 0)
    if src_image is None:
        raise FileNotFoundError(f"Image file {image} not found.")
    blurred = cv2.GaussianBlur(src_image, (7, 7), 0)
    th3 = cv2.adaptiveThreshold(blurred, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                thresholdType=cv2.THRESH_BINARY, blockSize=9, C=2)
    return th3

# Path to the image file
image = r'F:\Fun Project(Python)\image1.jpg'

# Check if the file exists
if not os.path.exists(image):
    raise FileNotFoundError(f"Image file {image} not found.")

im = cv2.imread(image, 0)
th3 = outline(image)

plt.imshow(th3, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()

WIDTH = im.shape[1]
HEIGHT = im.shape[0]
print(WIDTH, HEIGHT)

CUTOFF_LEN = ((WIDTH + HEIGHT) / 2) / 60  # 60 threshold value

# Corrected np.where usage
y_indices, x_indices = np.where(th3 == 0)
x_indices = x_indices - WIDTH / 2
y_indices = -1 * (y_indices - HEIGHT / 2)
positions = [list(iwh) for iwh in zip(x_indices, y_indices)]

win = turtle.Screen()
win.bgcolor('black')

t = turtle.Turtle()
t.color("brown")
t.shapesize(1)
t.pencolor("gray30")

t.speed(0)
turtle.tracer(0, 0)
t.penup()
t.goto(positions[0])
t.pendown()

time.sleep(3)

p = positions[0]
while positions:
    p = find_closest(p, positions)
    if p:
        current_pos = np.asarray(t.pos())
        new_pos = np.asarray(p)
        length = np.linalg.norm(new_pos - current_pos)
        if length < CUTOFF_LEN:
            t.goto(p)
            turtle.update()
        else:
            t.penup()
            t.goto(p)
            t.pendown()
        positions.remove(p)
    else:
        break

time.sleep(3)
turtle.bye()
