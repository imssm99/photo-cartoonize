import cv2 as cv
import numpy as np

box = lambda x: np.ones((x, x), dtype=np.uint8)

def cartoonize(img):
    # Detect edges in the image
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    edge = cv.Canny(blur, 600, 1200, apertureSize=5)
    #edge = cv.dilate(edge, box(3))

    # Apply bilateral filter to the image
    color = cv.bilateralFilter(img, 10, 100, 3)

    # Combine the color image with the edges
    edge_color = cv.cvtColor(edge, cv.COLOR_GRAY2BGR)
    cartoon = cv.bitwise_and(color, 255-edge_color)
    
    return cartoon