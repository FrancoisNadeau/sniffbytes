#!usr/bin/env/python3

import os
from typing import Union
from .get_bencod import get_bencod
from .get_bytes import get_bytes
from .has_enc import has_enc

def get_has_header(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None
) -> bool:
    """Returns True if 1st line of inpt is a header line
    Parameters
    ----------
    inpt: Bytes stream from buffer or file
            - See help(snif.get_bytes)
    - Optional
    ----------
    encoding: Character encoding of the bytes in buffer"""
    inpt = get_bytes(inpt)
    return [bool(inpt.splitlines()[0]
            not in bytes(".-0123456789",
                         has_enc(inpt, encoding)))
            if len(inpt.splitlines()) > 1 else False][0]

def main():
    if __name__ == __main__:
        get_has_header(inpt, encoding)

