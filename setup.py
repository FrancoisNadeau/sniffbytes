#!usr/bin/env/python3

import setuptools
from setuptools import setup

setup(
    name='sniffbytes',
    version='0',
    author='francois',
    author_email='francois.nadeau.1@umontreal.ca',
    description='Python3 data parsing and cleaning module',
    long_description="Python3 module featuring sniff_bytes.py,a dialect finder meant to increase the scope of CSV.Sniffer's supported input types and avoid crashes",
    long_description_content_type='text/x-rst',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    url='https://github.com/FrancoisNadeau/sniffbytes.git',
    python_requires=">=3.6",
)
