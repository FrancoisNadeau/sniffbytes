#!usr/bin/env/python3

import os
from unidecode import unidecode
from io import BytesIO
from typing import Union
import pandas as pd
from pandas import DataFrame as df
from .evenodd import evenodd
from .get_bytes import get_bytes
from .get_delimiter import get_delimiter
from .has_dpi import has_dpi
from .has_enc import has_enc
from .has_hdr import has_hdr
from .has_ltr import has_ltr

def bytes2df(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None,
    lineterminator: bytes = None,
    delimiter: bytes = None,
    has_header: bool = None,
    **kwargs: Union[
        bytes, bytearray, str, dict, object, map, list, tuple, os.PathLike, pd.DataFrame
    ]
) -> pd.DataFrame:
    """Converts a bytes object to a pd.DataFrame object
    ------------------------------------------------
    Parameters
    ----------
    inpt: Bytes stream from buffer or file
            - See help(snif.get_bytes).
    -----------------------------------
    - Optional
    ----------
    encoding: Character encoding of the bytes in buffer.
    has_header: True if first line is a header, else False.
    delimiter: Bytes (in native file encoding) representation
                of the value used as delimiter.
    dup_index: True if 'inpt' has duplicated index values, else False.
    lineterminator: Bytes representation in native file encoding
                    of the line termination character."""
    has_header = has_hdr(inpt, encoding, has_header)
    return [df((line.split() for line in unidecode(
               clean_bytes(inpt, **kwargs).decode()).splitlines()),
               dtype=object).T.set_index(0, drop=True).T
            if has_header
            else df((line.split() for line in unidecode(
                     clean_bytes(inpt, **kwargs).decode()).splitlines()),
                    dtype=object)][0]

def main():
    if __name__ == __main__:
        bytes2df(inpt, encoding, lineterminator, delimiter, has_header, **kwargs)

