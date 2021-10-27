#!usr/bin/env/python3

import chardet
import os
from collections import Counter
from typing import Union
from chardet import UniversalDetector as udet
from sniffbytes.get_bytes import get_bytes

def get_bencod(
    inpt: Union[bytes, bytearray, str, os.PathLike, object]
) -> str:
    """Returns the character encoding of 'inpt' as a string
    ----------------------------------------------------
    Parameters
    ----------
    inpt: Bytes from memory or file path pointing to a file
          file object ot be read as raw stream of bytes
          in native file character encoding"""
    inpt = get_bytes(inpt)
    detector = udet()
    detector.reset()
    feeder = (detector.feed(line) for
              line in inpt.splitlines(keepends=True))
    criteria = (detector.done, hasattr(detector, 'result'),
                detector.result["confidence"] > 0.75,
                detector.result["encoding"] is not None)
    while True:
        try:
            next(feeder)
            if not all(criteria):
#         if bool(not detector.done and not detector.result
#                 and detector.result["confidence"] > 0.75
#                 and detector.result["encoding"] is not None
#         ):
                continue
            else:
                break
#             break
            detector.close()
            result = detector.result["encoding"]
            break
        except StopIteration:
            result = tuple(dict(Counter(chardet.detect(line)['encoding'] for line in
                       inpt.splitlines(keepends=True)).most_common(1)).keys())[0]
            break
    if result == 'ascii':
        try:
            inpt.decode(result)
        except UnicodeEncodeError:
            try:
                result = "UTF-8"
                inpt.decode(result)
            except UnicodeEncodeError:
                try:
                    result = "ISO-8859-1"
                    inpt.decode(result)
                except UnicodeEncodeError:
                    result = "Latin-1"
    return result
  

def main():
    if __name__ == __main__:
        get_bencod(inpt)
