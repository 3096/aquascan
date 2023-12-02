import cv2

def canny(image):
    # Canny Edge Detection
    # image: image matrix
    # return: image matrix after Canny Edge Detection
    canny = cv2.Canny(image, 50, 240)
    return canny
