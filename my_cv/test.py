import cv2
from picamera.array import PiRGBArray
import numpy as np


def nothing():
    pass


cv2.namedWindow("颜色")
cv2.createTrackbar("B", "颜色", 0, 255, nothing)
cv2.createTrackbar("G", "颜色", 0, 255, nothing)
cv2.createTrackbar("R", "颜色", 0, 255, nothing)

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

raw_capture = PiRGBArray(camera, size=(640, 480))

for frame in camera.capture_continuous(raw_capture,
                                       format="bgr",
                                       use_video_port=True):
    image = frame.array

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    B = cv2.getTrackbarPos("B", "颜色")
    G = cv2.getTrackbarPos("G", "颜色")
    R = cv2.getTrackbarPos("R", "颜色")

    green = np.uint8([[[B, G, R]]])
    hsvGreen = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    lowerLimit = np.uint8([hsvGreen[0][0][0] - 10, 100, 100])
    upperLimit = np.uint8([hsvGreen[0][0][0] + 10, 255, 255])
    mask = cv2.inRange(hsv, lowerLimit, upperLimit)
    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("frame", image)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    key = cv2.waitKey(1)
    raw_capture.truncate(0)

    if key == 27:
        break

