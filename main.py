import utils

from algorithms.Gaussian_Filter_Images.gaussian import gaussian_filter
from algorithms.Sobel_Filter_Images.sobel import sobel_filter
from algorithms.Canny_Images.canny import canny
from algorithms.Hough_Transform_Images.hough_transform import hough_circle_transform

if __name__ == '__main__':
    
    # Runs the Gaussian Blur process on the starting images
    utils.process_dir('20_ARMS_JPEGS/', '.jpg', 'algorithms/Gaussian_Filter_Images/', '.png', gaussian_filter)

    # Runs the Sobel Filter function on the Gaussian Blur images
    utils.process_dir('algorithms/Gaussian_Filter_Images/', '.png', 'algorithms/Sobel_Filter_Images/', '.png', sobel_filter)

    # Canny Edge Detection
    utils.process_dir('algorithms/Gaussian_Filter_Images/', '.png', 'algorithms/Canny_Images/', '.png', canny)

    # Runs the Hough Transform function on the Gaussian Blur images
    # utils.process_dir('algorithms/Gaussian_Filter_Images/', '.png', 'algorithms/Hough_Transform_Images/', '.png', hough_circle_transform)
