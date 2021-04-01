#!usr/bin/env/python3

import os
import pandas as pd
from typing import Union
from .get_bytes import get_bytes
from .has_enc import has_enc
from .has_hdr import has_hdr
from .hdr_acc import hdr_acc

def get_widths(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None,
    has_header: bool = None,
) -> Union[str, int]:
    """Returns an integer corresponding to the longest line in
    bytes buffer that is not a header, which could include
    extra bytes such as commments
    -----------------------------
    Parameters
    ----------
    inpt: Bytes stream from buffer or file
            - See help(snif.get_bytes)
    ----------------------------------
    - Optional
    ----------
    encoding: Character encoding of the bytes in buffer"""
    inpt = get_bytes(inpt)
    encoding = has_enc(inpt, encoding)
    lines = [inpt.splitlines()[1:]
             if has_hdr(inpt, has_header, has_enc(inpt, encoding))
             else inpt.splitlines()][0]
    return [pd.Series((len(line) for line
            in lines)).dropna().max() if len(lines) >1 else
            len(inpt)][0]

def main():
    if __name__ == __main__:
        get_widths(inpt, encoding, has_header)
