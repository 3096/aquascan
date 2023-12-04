import cv2
import numpy as np

def image_contrast(image):
    # Image Contrast Filter
    # image: image matrix
    # return: image matrix after CLAHE algorithm
    # This is something called contrast limited adaptive histogram equalization
    # This will prove the image's contrast

    #LAB Color space 
    #l channel is lightness
    #a channel is change between red and green
    #b channel is change between yellow and blue
    lab= cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    lab_l_channel, lab_a_channel, lab_b_channel = cv2.split(lab)

    # Start CLAHE
    # Applying CLAHE to L-channel
    # This is because 
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl = clahe.apply(lab_l_channel)

    # merge the CLAHE enhanced L-channel with the a and b channel
    result = cv2.merge((cl,lab_a_channel,lab_b_channel))

    # Converting image from LAB Color model to BGR color space
    result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)

    return result
