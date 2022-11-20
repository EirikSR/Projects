
""" 
Args:
    Required:
        -f FILE, --file FILE: Path to image to be processed.
        -o OUT, --out OUT: The path to write the processed image to.

        either:
            -g, --gray: selects grayscale filter
        or:
            -se, --sepia: selects sepia filter
    Optional:
        --help, -h (flag, optional): Prints help text.
        --implement {...}, -i {python, numpy, numba} (optional):
            Determines which implementation of the three  modules to use -
            {python, numpy, numba}.
        -sc SCALE, --scale SCALE: Scale factor to resize image
        -k SEPIA_PERCENT, --sepia_k SEPIA_PERSENT: persentage of sepia effect

Examples:
    $ python instapy.py -h
    $ python instapy.py infile.jpg outfile.jpg
    $ python instapy.py -i python infile.jpg outfile.jpg

Dependencies:
    cv2
    Local:
        python_color2gray
        python_color2sepia
        numba_color2gray
        numba_color2sepia
        numpy_color2gray
        numpy_color2sepia
"""

import cv2
from argparse import ArgumentParser
from instapy import python_color2gray, python_color2sepia, numba_color2gray, numba_color2sepia, numpy_color2gray, numpy_color2sepia

#modules
modules_gray = [python_color2gray, numba_color2gray, numpy_color2gray]
modules_sepia = [python_color2sepia, numba_color2sepia, numpy_color2sepia]

"""
Writing the recognized arguments as well as help prompts
"""
parser = ArgumentParser(
    description ="Instapy"
)

parser.add_argument("-f", "--file",
                    
                    help="path of image source file", metavar="input_file")
parser.add_argument("-o", "--out",
                    help="path of image destination file",
                    metavar="destination_file")
parser.add_argument("-i", "--implement",
                    type=int,
                    help="choose implementation " +
                    "1 (python) 2 (numpy) or  3 (numba) " +
                    "- set to numpy by default",
                    metavar = "implement",
                    choices=range(1, 4), default=2)
parser.add_argument("-sc", "--scale",
                    help="scale factor of new image",
                    metavar="scale")
parser.add_argument("-k", "--sepia_k",
                    help="Percentage of sepia effect",
                    metavar="sepia factor")

parser.add_argument("-se", "--sepia",
                    action="store_true",
                    help="Select sepia filter")
parser.add_argument("-g", "--gray",
                    action="store_true",
                    help="select gray filter")

args = parser.parse_args()

def _grayscale_image(input_file, output_file,implement , scale):
    """ Takes a directory paths leading to image, then savess the grayscale version of the image using specified aproach aproach
     
    Args:
        input_file (str): path to image
        output_file (str): path to where the image is saved
        implement (func): the function used for grayscaling
        scale (float, optional): factor used in rescaling image
        
    Writes:
        3d array with grayscale filter, shape (height, width, 1) to specified path
    """ 
    if scale is not None:
        scale = float(scale)
    else:
        scale = 1

    image = cv2.imread(input_file)
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = implement.grayscale(image, scale)

    cv2.imwrite(output_file, output)


def _sepia_image(input_file, output_file,implement, scale , k):
     """ Takes a directory paths leading to image, then saves the sepia version of the image using specified aproach aproach
     
    Args:
        input_file (str): path to image
        output_file (str): path to where the image is saved
        implement (func): the function used for sepia
        scale (float, optional): factor used in rescaling image
        k (float, optional): percentage of sepia effect on range 0-1
    Writes:
        3d array with sepia filter, shape (height, width, 1) to specified path
    """ 
    if scale is not None:
        scale = float(scale)
    else:
        scale = 1
    if k is not None:
        k = float(k)
    else:
        k = 1

    image = cv2.imread(input_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = implement.sepia(image, scale, k)

    cv2.imwrite(output_file, output)

try:
    if args.gray:
        _grayscale_image(args.file, args.out, modules_gray[args.implement-1], args.scale, args.sepia_k)
    if args.sepia:
        _sepia_image(args.file, args.out, modules_sepia[args.implement-1], args.scale, args.sepia_k)
except ValueError as v:
    parser.error(v)