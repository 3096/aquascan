import cv2

def canny(image):
    # Canny Edge Detection
    # image: image matrix
    # return: image matrix after Canny Edge Detection
    # L2Gradient is using the normalization that we used in the original c in class which is the more accurate gradient
    # L1 norm = Sqrt((dI/dx)^2 + (dI/dy)^2) VS when it is marked false: L2 norm = |dI/dx| + |dI/dy|
    canny = cv2.Canny(image, 50, 240, L2gradient=True)
    return canny
