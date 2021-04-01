#!usr/bin/env/python3

import os
from typing import Union
from .has_enc import has_enc
from .get_lineterminator import get_lineterminator

def has_ltr(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None,
    lineterminator: bytes = None
) -> bytes:
    return [lineterminator if lineterminator is not None
            else get_lineterminator(inpt, has_enc(inpt, encoding))][0]

def main():
    if __name__ == __main__:
        has_ltr(inpt, encoding, lineterminator)
