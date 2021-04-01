#!usr/bin/env/python3

import os
from typing import Union
from .get_bytes import get_bytes
from .get_delimiter import get_delimiter
from .get_dup_index import get_dup_index
from .get_lineterminator import get_lineterminator
from .get_widths import get_widths
from .has_enc import has_enc
from .has_hdr import has_hdr
from .has_ltr import has_ltr

def sniff_bytes(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None,
    has_header: bool = None,
    lineterminator: bytes = None
) -> dict:
    """Returns a dictionary containing informations about datas from
    a readable file or buffer of raw bytes.
    ---------------------------------------
    Order is as folllows:
        ("encoding", "delimiter", "has_header", "dup_index",
         "lineterminator", "nfields", "width", "nrows").
    ----------------------------------------------------
    Information is similar to csv.dialect objects.
    The outout is designed to work well with common data structures,
    including, bu not restricted to:
        - CSV, Pandas, _io buffers, arrays etc.
    -------------------------------------------
    See each function's help details individually:
        inpt = help(sniffer.get_bytes)
        encoding = help(sniffer.get_bencod)
        has_header = help(sniffer.get_has_header)
        delimiter = help(sniffer.get_delimiter)
        lineterminator = help(sniffer.get_lineterminator)
        dup_index = help(snif.dup_index)"""
    inpt = get_bytes(inpt)
    encoding = has_enc(inpt, encoding)
    has_header = has_hdr(inpt, encoding, has_header)
    lineterminator = has_ltr(inpt, encoding, lineterminator)
    return dict(
        zip(("encoding", "delimiter", "has_header",
             "dup_index", "lineterminator",
             "width", "nrows"),
            (encoding,
             get_delimiter(inpt, encoding, lineterminator),
             has_header,
             get_dup_index(inpt, encoding, has_header),
             lineterminator,
             get_widths(inpt, encoding, has_header),
             len(inpt.splitlines()))))

def main():
    if __name__ == __main__:
        sniff_bytes(inpt, encoding, has_header)
