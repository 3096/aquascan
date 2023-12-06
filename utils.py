import os

import cv2


def process_dir(dir_path, ext, output_path, output_ext, algorithm):
    """
    Process all files in a directory with a given extension.
    """
    for filename in os.listdir(dir_path):
        if filename.lower().endswith(ext):
            cv2.imwrite(os.path.join(output_path, os.path.splitext(filename)[0] + output_ext),
                        algorithm(cv2.imread(os.path.join(dir_path + filename))))
