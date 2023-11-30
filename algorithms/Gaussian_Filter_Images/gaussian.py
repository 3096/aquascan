import cv2

def gaussian_filter(image):
    # Gaussian Filter
    # image: image matrix
    # return: image matrix after Gaussian Filter
    gaussian = cv2.GaussianBlur(image, (5, 5), 0)
    return gaussian
