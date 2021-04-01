#!usr/bin/env/python3

import os
from typing import Union
import pandas as pd
from .get_bytes import get_bytes
from .has_enc import has_enc
from .has_hdr import has_hdr

def get_nfields(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None,
    has_header: bool = None,
) -> bytes:
    """Returns a bytes representation of an integer corresponding
    to the maximal number of fields in the bytes stream lines
    for lines that are not a header.
    --------------------------------
    Parameters
    ----------
    inpt: Bytes stream from buffer or file
            - See help(snif.get_bytes).
    -----------------------------------
    - Optional
      --------
    has_header: True if first line is a header, else False."""
    inpt = get_bytes(inpt)
    has_header = has_hdr(inpt, has_enc(inpt, encoding), has_header)
    inpt = [inpt.splitlines()[1:] if has_header else inpt.splitlines()][0]
    return pd.Series(len(line.split()) for line in inpt).max()

def main():
    if __name__ == __main__:
        get_nfields(inpt, encoding, has_header)
