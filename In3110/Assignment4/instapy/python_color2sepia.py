import cv2
import numpy as np
import time

scriptname = "python_color2sepia"


def sepia(image, scale=1, k=1):
     """ 
     Takes a 3d array and returns the sepia version 3d array of the image using regilar python iterative aproach
     
    Args:
        image (array): 3d array containing an image with shape (height, width, 3)
        scale (float, optional): Factor of rescaling
        k (flloat, optioal): percentage of sepia effect as a float between 0 and 1
    Returns:
        3d array with sepia filter, shape (height, width, 3)
    """ 
    sepia_matrix = np.mat(
    [
        [0.393 + 0.607 * (1 - k), 0.769 - 0.769 * (1 - k), 0.189 - 0.189 * (1 - k)],
        [0.349 - 0.349 * (1 - k), 0.686 + 0.314 * (1 - k), 0.168 - 0.168 * (1 - k)],
        [0.272 - 0.349 * (1 - k), 0.534 - 0.534 * (1 - k), 0.131 + 0.869 * (1 - k)],
    ]
    )
    
    image = cv2.resize(image, (0, 0), fx=scale, fy=scale)
    shape = image.shape
    output = np.zeros((shape[0], shape[1], 3))

    for i in range(shape[0]):
        for j in range(shape[1]):
            a = image[i][j].reshape(-1, 1)
            # print(a)
            b = (sepia_matrix * a).reshape((3,))
            output[i][j] = np.array(
                (min(b[0, 2], 255), min(b[0, 1], 255), min(b[0, 0], 255))
            )

    output = output.astype("uint8")

    return output

if __name__ == "__main__":
    """
    If the script is ran, the program will run the function 3 times in order to time it. 
    Finally the picture will be saved and a report regarding the time will be printed and saved in report folder
    """

    filename = "bliss.png"
    outputname = filename.split(".")[0] + "_sepia.jpeg"

    image = cv2.imread(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    N = 3

    t0 = time.time()
    for i in range(N):
        pic = sepia(image)
    t1 = time.time()

    avg_time = (t1 - t0) / N

    string = f"Timing: {scriptname}\nAverage runtime running {scriptname} after {N} runs: {avg_time}s\nTiming performed using : {image.shape}"

    print(string)
    # Save string as report:
    with open("Reports/" + scriptname.split(".")[0] + "_report.txt", "w") as text_file:
        text_file.write(string)
        text_file.close()

    cv2.imwrite(outputname, pic)