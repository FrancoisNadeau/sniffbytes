#!usr/bin/env/python3

import os

def stream2file(
    inpt: Union[bytes, bytearray, str, os.PathLike, object],
    dst_path: Union[str, os.PathLike],
) -> None:
    """Save bytes stream buffer to file.
    ---------------------------------
    Parameters
    ----------
    inpt: Bytes stream buffer or file path to read bytes from.
    dst_path: Path pointing to desired save location"""
    with open(dst_path, "wb") as binary_file:
        binary_file.write(inpt)
        binary_file.close()

def main():
    if __name__ == __main__:
        stream2file(inpt, dst_path)

