import cv2
import numpy as np
import time

scriptname = "python_color2gray"


def grayscale(image, scale=1):
     """ Takes a 3d array and returns the grayscale version 3d array of the image using regular python iterative aproach
     
    Args:
        image (str): 3d array containing an image with shape (height, width, 1)
        scale (float, optional): Factor of rescaling
    Returns:
        3d array with grayscale filter, shape (height, width, 1)
    """ 
    image = cv2.resize(image, (0, 0), fx=scale, fy=scale)

    shape = image.shape
    output = np.zeros((shape[0], shape[1], 1))

    for i in range(shape[0]):
        for j in range(shape[1]):
            output[i][j][0] = (
                0.21 * image[i][j][0] + 0.72 * image[i][j][1] + 0.07 * image[i][j][2]
            )

    output = output.astype("uint8")
    return output

if __name__ == "__main__":
    """
    If the script is ran, the program will run the function 3 times in order to time it. 
    Finally the picture will be saved and a report regarding the time will be printed and saved in report folder
    """


    filename = "bliss.png"
    outputname = filename.split(".")[0] + "_greyscale.jpeg"
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