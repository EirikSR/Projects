# IN3110-eiriksro
## README eiriksro Assignment4

### PACKAGE
##### Name
(directory)
```
instapy
```

##### Methods
```
grayscale([input file path], [output file path (optional)])
sepia([input file path], [output file path (optional)])
```
Reads an image from file path,
either creates grayscale/sepia version the image,
optionally saves the filtered image to a given destination path.
The method also returns a  3d array(int) representing the filterd picture.


#### Requirements (specified in setup.py)
- ```numba```
- ```numpy```
- ```opencv-python```
- ```pytest```

#### Local installation
from the top direcory (IN3110-eiriksro/Assignment4, directory containing setup.py and README.md)
```bash
$ pip install .
```

### Useage (after installation)
see documentation for ```instapy```
examples:
``` python
>>> import instapy
>>> instapy.grayscale_image("input.jpg", "output.jpg"(optional))
>>> instapy.sepia_image("input.jpg", "output.jpg"(optional))
```

#### RUN TESTS
using testing framework ```pytest```
tests ```instapy``` package
from the top direcory (IN3110-eiriksro/Assignment4, directory containing setup.py and README.md)
```bash
$ pytest
```

#### RUNNING/USING OTHER SCRIPTS
all python scripts are located in the package directory,
but not all of them are used in the package (blur_1, blur_3, blur, blur_faces are excluded)

```
instapy
```
Command line user interface - see docstring in instapy/instapy.py
Example (Creates a grayscaled version of PATH1 and saves to PATH2):
```bash
$ python -m instapy.instapy -i 2 -f PATH1 -o PATH2 -g
$ python -m instapy.instapy -h (get help string)
```

### Other modules
Import as regular modules
(only ```grayscale_image(), sepia_image()```) is part of the package
see docstrings for more information about modules and methods
```
python_color2gray, python_color2sepia, numba_color2gray, numba_color2sepia, numpy_color2gray, numpy_color2sepia
```
example:
```python
>>> python_color2gray.grayscale(img_array, scale)
>>> numpy_color2sepia.sepia(img_array, scale)
```

#### ADDITIONAL FILES/DIRECTORIES
```
instapy
```
Contains all python scripts except setup.py to enable packaging
```
instapy/tests
```
Contains the test file test.py to test package functions
