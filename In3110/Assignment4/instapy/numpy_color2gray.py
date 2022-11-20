import cv2
import numpy as np
import time

scriptname = "numpy_color2gray"


def grayscale(image, scale=1):
    """Takes a 3d array of an image and turns in into a grayscaled version
        if a scale is provided, the function will reshape
    """
    image = cv2.resize(image, (0, 0), fx=scale, fy=scale)
    output = 0.21 * image[:, :, 0] + 0.72 * image[:, :, 1] + 0.07 * image[:, :, 2]
    output = output.astype("uint8")
    output = output.reshape(image.shape[0], image.shape[1], 1)
    return output

if __name__ == "__main__":

    """ Takes a 3d array and returns the grayscale version 3d array of the image using numpy vectorized aproach
     
    Args:
        image (array): 3d array containing an image with shape (height, width, 1)
        scale (float, optional): Factor of rescaling
    Returns:
        3d array with grayscale filter, shape (height, width, 1)
    """ 


    filename = "bliss.png"
    outputname = filename.split(".")[0] + "_greyscale2.jpeg"
    image = cv2.imread(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    N = 3

    t0 = time.time()
    for i in range(N):
        pic = grayscale(image)
    t1 = time.time()

    avg_time = (t1 - t0) / 3

    string = f"Timing: {scriptname}\nAverage runtime running {scriptname} after {N} runs: {avg_time}s\nTiming performed using : {image.shape}"

    print(string)
    # Save string as report:
    with open("Reports/" + scriptname.split(".")[0] + "_report.txt", "w") as text_file:
        text_file.write(string)
        text_file.close()

    cv2.imwrite(outputname, pic)