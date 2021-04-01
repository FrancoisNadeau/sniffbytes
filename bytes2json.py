#!usr/bin/env/python3

import json
import os
from typing import Union

def bytes2json(apath: Union[str, os.PathLike]) -> dict:
    with open(apath, 'rb', buffering = 0) as jfile:
        jbytes = json.load(jfile)
    jfile.close()
    return dict(jbytes)

def main():
    if __name__ == __main__:
        bytes2json(apath)
