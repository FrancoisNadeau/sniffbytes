#!usr/bin/env/python3

import os
from typing import Union
import pandas as pd
from pandas import DataFrame as df
from load_utils.evenodd import evenodd
from .get_bytes import get_bytes
from .get_delimiter import get_delimiter
from .has_enc import has_enc
from .has_hdr import has_hdr
from .has_ltr import has_ltr

def fix_dup_index(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    encoding: str = None,
    lineterminator: bytes = None,
    delimiter: bytes = None,
    keep_delim: bool = False,
    keep_lterm: bool = False
) -> bytes:
    """Fixes files where indexes are duplicated.
    -----------------------------------------
    Parameters
    ----------
    inpt: Bytes stream from buffer or file
            - See help(snif.get_bytes).
    -----------------------------------
    - Optional
    ----------
    encoding: Character encoding of the bytes in buffer.
    delimiter: Bytes (in native file encoding) representation
                of the value used as delimiter."""
    inpt = get_bytes(inpt)
    encoding = has_enc(inpt, encoding)
    lineterminator = [has_ltr(inpt, encoding, lineterminator)
                      if keep_lterm else b"\n"][0]
    ndlm = [get_delimiter(inpt, encoding,
                          has_ltr(inpt, encoding, lineterminator))
            if keep_delim else b"\t"][0]
    evdf, oddf = (df((line.split() for line in lines),
                     dtype=object) for lines in
                  evenodd(inpt.splitlines()))
    booltest = [itm[0] for itm in enumerate(tuple(zip(
                    [itm[1] for itm in evdf.iteritems()],
                    [itm[1] for itm in oddf.iteritems()])))
                if all(itm[1][0].values == itm[1][1].values)]
    datas = pd.concat((evdf[booltest],
                       pd.concat(
                           list(itm[1] for itm in
                                evdf.iteritems())[booltest[-1] \
                                                  + 1 : -1], axis=1),
            pd.concat(list(itm[1] for itm in
                           oddf.iteritems())[booltest[-1] + 1 :],
                      axis=1),),axis=1,)
    try:
        return lineterminator.join(
                   ndlm.join(
                       itm if isinstance(itm, bytes)
                       else str(np.nan).encode(encoding)
                       for itm in row[1].values.tolist())
            for row in datas.iterrows())
    except IndexError:
        return inpt

def main():
    if __name__ == __main__:
        fix_dup_index(inpt, encoding, lineterminator,
                      delimiter, keep_delim, keep_lterm)
