import os
import numpy as np
import cv2
import pytest
from instapy import python_color2gray, python_color2sepia, numba_color2gray, numba_color2sepia, numpy_color2gray, numpy_color2sepia



img_size = 100

test_file = "test.jpg"

np.random.seed(0)

def _generate_test_image(test_file):
    """ Private method that generates test image to use for testing.
    Writes image to temporary image file, and returns 3d array representing the image
    
    Args:
        test_file (str): the temporary path in the test folder
    Yields:
        int[][][]: 3d array representing the generated image
    """

    image = np.random.uniform(low = 0, high = 255, size=(img_size, img_size, 3))
    cv2.imwrite(test_file, image)

    output = image.astype("uint8")
    return output


def _remove_test_image():
    """Removes generated test image from the working directory
    """
    if os.path.exists(test_file):
        os.remove(test_file)

image = _generate_test_image(test_file)

@pytest.mark.parametrize(
    "output", [(python_color2gray.grayscale(image)),
               (numpy_color2gray.grayscale(image)),
               (numba_color2gray.grayscale(image))]
)
def test_grayscale(output):
    """Asserts that grayscale image has shape of one value per pixel, 
        Asserts that random grayspace pixel has expected value
    """

    i = np.random.randint(low=0, high=100)
    j = np.random.randint(low=0, high=100)
    pixel = image[i][j]
    expected =  int(0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2])
    assert output[i][j] == expected and output.shape == (img_size, img_size, 1)

@pytest.mark.parametrize(
    "output", [(python_color2sepia.sepia(image)),
               (numpy_color2sepia.sepia(image)),
               (numba_color2sepia.sepia(image))]
)
def test_sepia(output):
    """Asserts that sepia image has shape of one value per pixel, 
        Asserts that random sepia pixel has expected value
    """

    i = np.random.randint(low=0, high=100)
    j = np.random.randint(low=0, high=100)
    pixel = image[i][j]
    print(0.393*pixel[0]+ 0.769*pixel[1]+ 0.189*pixel[2])
    expected =  [0.393*pixel[0] + 0.769*pixel[1] + 0.189*pixel[2],
                 0.349*pixel[0] + 0.686*pixel[1] + 0.168*pixel[2],
                 0.272*pixel[0] + 0.534*pixel[1] + 0.131*pixel[2]]
    print(expected)
    expected = np.array(expected).astype("uint8")[::-1]
    
    print(output[i][j], expected)
    assert (output[i][j] == expected).all() and output.shape == (img_size, img_size, 3)

_remove_test_image()