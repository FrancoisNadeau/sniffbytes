#!usr/bin/env/python3

import os
from io import BytesIO
from typing import Union
from load_utils.evenodd import evenodd
from .get_bytes import get_bytes
from .get_delimiter import get_delimiter
from .has_dpi import has_dpi
from .has_enc import has_enc
from .has_hdr import has_hdr
from .has_ltr import has_ltr

def clean_bytes(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None,
    has_header: bool = None,
    lineterminator: bytes = None,
    delimiter: bytes = None,
    dup_index: bool = None,
    **kwargs: Union[
        bytes, bytearray, str, dict, object, map, tuple, os.PathLike, pd.DataFrame
    ]
) -> bytes:
    """Returns a clean (suitable for StringIO and Pandas modules)
    bytes stream buffer with fixed 'missing' missing values.
    --------------------------------------------------------
    Takes into account:
        - Incorrect missing values representation
        - Duplicated indexes
        - Inconsistent delimiters
        - Within-values inconsistencies
              - (e.g. using a variable amount of whitespaces
                 to delimiterarate values within a same file or stream.
        - If file has a header row with labels or not
        - Variable source or native character encodings
    Bonus: Files can be read from ZipFile archives
        - See 'scanzip.py'
    ----------------------
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
    lineterminator: Bytes representation in native file encoding
                    of the line termination character.
    dup_index: True if 'inpt' has duplicated index values, else False."""
    inpt = get_bytes(inpt)
    encoding = has_enc(inpt, encoding)
    lineterminator = has_ltr(inpt, encoding, lineterminator)    
    has_header = has_hdr(inpt, encoding, has_header)
    delimiter = [delimiter if delimiter is not None
                 else get_delimiter(inpt, encoding, lineterminator)][0]
    dup_index = has_dpi(inpt, encoding, has_header)
    newsheet = BytesIO(b"\n".join(
                   [b"\t".join(itm.strip(b" ")
                               for itm in re.sub(
                                   b" " + b"{2,}", b" " + \
                                   delimiter + b" ",
                                   line).split(delimiter))
                    for line in fix_na_reps(get_bytes(inpt).lower(),
                                            encoding, delimiter,
                                            lineterminator)
                    .decode("utf8", "replace").replace("�", "").strip()
                    .encode("utf8").splitlines()]))
    return [fix_dup_index(newsheet.read(), encoding)
            if dup_index else newsheet][0]

def main():
    if __name__ == __main__:
        clean_bytes(inpt, encoding, has_header, lineterminator,
                      delimiter, dup_index, **kwargs)

