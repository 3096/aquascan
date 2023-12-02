import cv2

def sobel_filter(image):
    # Sobel Filter
    # image: image matrix
    # return: image matrix after Sobel Filter
    sobel = cv2.Sobel(image, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=3)
    return sobel
