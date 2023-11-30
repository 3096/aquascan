import utils

from algorithms.Gaussian_Filter_Images.gaussian import gaussian_filter

if __name__ == '__main__':
    utils.process_dir('20_ARMS_JPEGS/', '.jpg',
                      'algorithms/Gaussian_Filter_Images/', '.png', gaussian_filter)
