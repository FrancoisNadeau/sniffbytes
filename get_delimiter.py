#!usr/bin/env/python3

import os
from collections import Counter
import regex
import string
from typing import Union
import pandas as pd
from sniffbytes.get_bytes import get_bytes
from sniffbytes.has_enc import has_enc
from sniffbytes.has_ltr import has_ltr

def check_delims(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None
) -> bytes:
    """ Returns a generator to speed-up get_delimiter function """
    inpt = get_bytes(inpt)
    encoding = has_enc(inpt, encoding)
    inpt = string.capwords(inpt.decode(encoding)).encode(encoding)
    return  Counter(
                pd.Series(pd.Series(pd.Series(
                    next(
                        (regex.sub(bytes("|", encoding).join(
                        map(regex.escape, itm[1])),
                                    bytes("|", encoding),
                                    itm[0])
                          for itm in
                          tuple(zip(inpt.splitlines(),
                                    [line.replace(
                                        bytes("\x00", encoding),
                                        bytes("", encoding)).split()
                                     for line in
                                     bytes("\n", encoding).join(
                                         inpt.splitlines()).split(
                                             bytes("\n", encoding))])))
                        )).unique().max().split(
                    bytes("\\", encoding))).unique()[0].split(
                        bytes("|", encoding))[1:],
                          dtype="object").unique()
                    ).most_common(1).__iter__()

def get_delimiter(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None,
    lineterminator: bytes = None,
) -> bytes:
    """Returns the character used as delimiter within
    the bytes stream buffer in native character encoding
        - Replaces csv.Sniffer,
          which raises an error upon failure
              - Failure happens frequently for files
                containing any writing or formatting mistake
    --------------------------------------------------------
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
    delimiters = tuple(check_delims(inpt, encoding))
    try:
        return [b" " if bool(delimiters[0] == b"" and b" ")
                else delimiters[0]][0]
    except IndexError:
        return has_ltr(inpt, encoding, lineterminator)

def main():
    if __name__ == __main__:
        get_delimiter(inpt, encoding, lineterminator)

