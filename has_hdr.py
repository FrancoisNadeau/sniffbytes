#!usr/bin/env/python3

from .has_enc import has_enc
from .get_has_header import get_has_header

def has_hdr(
    inpt,
    encoding: str = None,
    has_header: bool = None
) -> bool:
    return [has_header if has_header is not None
            else get_has_header(inpt, has_enc(inpt, encoding))][0]

def main():
    if __name__ == __main__:
        has_hdr(inpt, encoding, has_header)

