import cv2
import numpy as np

def hough_circle_transform(image):
    # Gaussian Filter
    # image: image matrix
    # return: image matrix after Hough Circle transform

    #Convert to grayscale
    hough = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(hough, cv2.HOUGH_GRADIENT, 1.5, 30, param1=50, param2=70, minRadius=0, maxRadius=0)

    circles = np.uint16(np.around(circles))

    for c in circles[0, :]:
        #Outer Circle
        cv2.circle(hough, (c[0], c[1]), c[2], (0, 255, 0), 2)
        #Inner Circle
        cv2.circle(hough, (c[0], c[1]), 1, (0, 0, 255), 3)

    return hough
