import utils

from algorithms.Gaussian_Filter_Images.gaussian import gaussian_filter
from algorithms.Sobel_Filter_Images.sobel import sobel_filter

if __name__ == '__main__':
    
    #Runs the Gaussian Blur process on the starting images
    utils.process_dir('20_ARMS_JPEGS/', '.jpg',
                      'algorithms/Gaussian_Filter_Images/', '.png', gaussian_filter)
    
    #Runs the Sobel Filter function on the Gaussian Blur images
    utils.process_dir('algorithms/Gaussian_Filter_Images/', '.png', 'algorithms/Sobel_Filter_Images/', '.png', sobel_filter)