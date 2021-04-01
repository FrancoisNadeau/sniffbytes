#!usr/bin/env/python3

import os
from typing import Union
import pandas as pd
from .get_bytes import get_bytes
from .has_enc import has_enc

def get_lineterminator(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None
) -> bytes:
    """Returns the character used as line terminator within
    the bytes stream buffer in native character encoding

    Parameters
    ----------
    inpt: Bytes stream from buffer or file
            - See help(snif.get_bytes)"""
    inpt = get_bytes(inpt)
    encoding = has_enc(inpt, encoding)
    linterminator = pd.Series(
        next(
            (
                itm[0].strip(itm[1])
                for itm in tuple(zip(inpt.splitlines(keepends=True), inpt.splitlines()))
            )
        )
    ).unique()[0]
    return [linterminator if linterminator != "".encode(encoding)
            else "\n".encode(encoding)][0]

def main():
    if __name__ == __main__:
        get_lineterminator(inpt, encoding)
