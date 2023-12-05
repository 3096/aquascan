import cv2

def image_contrast(image):
    # Image Contrast Filter
    # image: image matrix
    # return: image matrix after CLAHE algorithm
    # This is something called contrast limited adaptive histogram equalization
    # This will improve the image's contrast by:
    # -computing a histogram of pixel intensities
    # -evenly distributing the most common pixels
    # -giving a linear trend to cumulative distribution function (turn into straight line)

    #Convert to LAB Color space 
    #l channel is lightness
    #a channel is change between red and green
    #b channel is change between yellow and blue
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    lab_l_channel, lab_a_channel, lab_b_channel = cv2.split(lab)

    # Start CLAHE
    # Applying CLAHE to l-channel
    # This is because CLAHE takes in a gray image, in this case just the lightness channel.
    # clip limiting is the threshold for limiting the contrast (reduce noise amplification)
    # tile grid size divides image to M x N tiles to apply equalization to each one.
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl = clahe.apply(lab_l_channel)

    # Merge new L-channel with the a and b channels
    result = cv2.merge((cl,lab_a_channel,lab_b_channel))

    # Convert image from LAB Color model to BGR color space
    result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)

    return result
