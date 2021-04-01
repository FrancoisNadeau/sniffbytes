#!usr/bin/env/python3

import os
from typing import Union
from .get_bytes import get_bytes
from .has_enc import has_enc
from .get_has_header import get_has_header

def hdr_acc(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None,
) -> bool:
    inpt = get_bytes(inpt)
    encoding = has_enc(inpt, encoding)
    return [inpt.splitlines()[1:] 
            if bool(get_has_header(inpt, has_enc(inpt, encoding))
                    and len(inpt).splitlines()) >1
            else inpt.splitlines()][0]
def main():
    if __name__ == __main__:
        hdr_acc(inpt, encoding, has_header)

