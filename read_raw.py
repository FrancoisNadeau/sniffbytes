#!usr/bin/env/python3

import os
from typing import Union

def read_raw(inpt: Union[str, os.PathLike]) -> bytes:
    with open(inpt, "rb", buffering = 0) as myfile:
        outpt = myfile.read()
    myfile.close()
    return outpt

def main():
    if __name__ == __main__:
        read_raw(inpt)
