#!usr/bin/env/python3

import os
import regex
from typing import Union
import numpy as np
from .get_bytes import get_bytes
from .get_delimiter import get_delimiter
from .get_lineterminator import get_lineterminator
from .has_enc import has_enc
from .has_hdr import has_hdr
from .has_ltr import has_ltr

def fix_na_reps(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None,
    delimiter: bytes = None,
    lineterminator: bytes = None,
) -> bytes:
    """Returns a version of the bytes buffer replacing any missing 'missing'
    values by automatically.
    To do so, the np.nan value, padded between whitespaces - all
    converted into native file encoding, are inserted where two or
    more consecutive delimiters are found.
    --------------------------------------
    Parameters
    ----------
    inpt: Bytes stream from buffer or file
            - See help(snif.get_bytes).
    -----------------------------------
    - Optional
      --------
    encoding: Character encoding of the bytes in buffer.
    delimiter: Bytes (in native file encoding) representation
               of the value used as delimiter.
    lineterminator: Bytes (in native file encoding) representation
                    of the value used as line terminator."""
    inpt = get_bytes(inpt)
    encoding = has_enc(inpt, encoding)
    lineterminator = has_ltr(inpt, encoding, lineterminator)    
    delimiter = [delimiter if delimiter else
                 get_delimiter(inpt, encoding, lineterminator)][0]
    return lineterminator.join(
               regex.sub(delimiter + "{2,}".encode(encoding),
                         delimiter + str(np.nan).encode(encoding) + delimiter,
                         line) for line in inpt.splitlines())

def main():
    if __name__ == __main__:
        fix_na_reps(inpt, encoding, delimiter, lineterminator)
