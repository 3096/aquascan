import cv2

def averaging_filter(image):
    # Averaging Filter
    # image: image matrix
    # return: image matrix after Averaging Filter
    averaging = cv2.blur(image,(15,15))
    return averaging
