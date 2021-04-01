#!usr/bin/env/python3

from .get_bencod import get_bencod
    
def has_enc(inpt, encoding: str = None):
    return [encoding if encoding else get_bencod(inpt)][0]

def main():
    if __name__ == __main__:
        has_enc(inpt, encoding)
