#!usr/bin/env/python3

import os
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
    while True:
        next((detector.feed(line) for line in inpt.splitlines()))
        if (
            not detector.done
            and not detector.result
            and detector.result["confidence"] > 0.75
            and detector.result["encoding"] is not None
        ):
            continue
        else:
            break
        break
    detector.close()
    result = detector.result["encoding"]
    if result == 'ascii':
        try:
            inpt.decode("UTF-8")
            return "UTF-8"
        except UnicodeEncodeError:
            try:
                inpt.decode("ISO-8859-1")
                return "ISO-8859-1"
            except UnicodeEncodeError:
                return result
    else:
        return result

def main():
    if __name__ == __main__:
        get_bencod(inpt)
