name="instapy"

import cv2
from instapy.numpy_color2gray import *
from instapy.numpy_color2sepia import *
import os

def grayscale_image(input_filename, output_filename=None):
    """ Creates grayscale version of an image from a given image file, and optionally writes the grayscale version to a given path.
    Args:
        input_filename (str): The path name for the image to grayscale.
        output_filename (str, optional): The path name the sepia image writes to.
    Returns:
        output(int[][][]): 3d array containing the resulting grayscale image.
    """
    if os.path.exists(input_filename):
        image = cv2.imread(input_filename)
    else:
        raise Exception("Path not found")
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    output = grayscale(image)

    if output_filename != None:
        cv2.imwrite(output_filename, output)
    return output

def sepia_image(input_filename, output_filename=None):
    """ Creates sepia version of an image from a given image file, and optionally writes the sepia version to a given path.
    Args:
        input_filename (str): The path name for the image to sepia.
        output_filename (str, optional): The path name the sepia image writes to.
    Returns:
        output(int[][][]): 3d array containing the resulting sepia image.
    """
    if os.path.exists(input_filename):
        image = cv2.imread(input_filename)
    else:
        raise Exception("Path not found")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = sepia(image)

    if output_filename != None:
        cv2.imwrite(output_filename, output)
    return output