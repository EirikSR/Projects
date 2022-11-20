from setuptools import setup
from setuptools import find_packages

setup(
    name="instapy",
    version="1.0",
    description="Containes grayscale and sepia filters",
    install_requires=[
            'numpy',
            'opencv-python',
            "numba",
            "pytest",
      ],
    author="Eiriksro",
    author_email=" eiriksro@student.matnat.uio.no",
    url="?",
    #packages=["code"],
    packages=find_packages(),
    # entry_point={}
)