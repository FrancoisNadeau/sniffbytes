#!usr/bin/env/python3

import os
from typing import Union
from .evenodd import evenodd
from .get_bytes import get_bytes
from .has_enc import has_enc
from .has_hdr import has_hdr

def get_dup_index(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None,
    has_header: bool = None,
) -> bool:
    """Returns True if the first item of each even and each
    odd line is repeated. Returns False otherwise or upon IndexError.
    As IndexError is raised when trying to access values by an index out
    of a sequence boundairies, IndexError indicates single-byte files.
    Being a single byte, it can't be a duplicate index.
    ---------------------------------------------------
    Parameters
    ----------
    inpt: Bytes stream from buffer or file
            - See help(snif.get_bytes).
    -----------------------------------
    - Optional
      --------
    has_header: True if first line is a header, else False
    delimiter: Bytes (in native file encoding) representation
               of the value used as delimiter."""
    inpt = get_bytes(inpt)
    has_header = has_hdr(inpt, has_enc(inpt, encoding), has_header)
    lines = [inpt.splitlines()[1:]
             if has_header else inpt.splitlines()][0]
    ev_items, od_items = evenodd(inpt.splitlines())
    try:
        return ev_items[0].split()[0] == od_items[0].split()[0]
    except IndexError:
        return False

def main():
    if __name__ == __main__:
        get_dup_index(inpt, encoding, has_header)
