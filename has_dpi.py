#!usr/bin/env/python3

import os
from typing import Union
from .get_bytes import get_bytes
from .get_dup_index import get_dup_index
from .has_enc import has_enc
from .has_hdr import has_hdr

def has_dpi(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None,
    has_header: bool = None
) -> bool:
    return [dup_index if dup_index is not None
            else get_dup_index(inpt, has_enc(inpt, encoding),
                               has_hdr(inpt, encoding, has_header))][0]
def main():
    if __name__ == __main__:
        has_dpi(inpt, encoding, has_header)

