import cv2
import numpy as np

def hough_circle_transform(image):
    # Hough Circle Transform
    # image: image matrix
    # return: image matrix after Hough Circle transform

    #Convert to grayscale
    hough = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(hough, cv2.HOUGH_GRADIENT, 1, 1800, param1=10, param2=30, minRadius=20, maxRadius=90)
    #circles = cv2.HoughCircles(hough,cv2.HOUGH_GRADIENT_ALT,1.5, 200, param1=50, param2=0.9, minRadius=0, maxRadius=500)


    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for c in circles[0, :]:
            #Outer Circle
            cv2.circle(image, (c[0], c[1]), c[2], (0, 255, 0), 2)
            #Inner Circle
            cv2.circle(hough, (c[0], c[1]), 1, (0, 0, 255), 3)

    return image
