#!/usr/bin/env python3.6

import PorterStemmer
from sys import argv, exit


def main():
    if len(argv) < 2:
        exit('Usage: ./stemWord word')

    ps = PorterStemmer.PorterStemmer()
    print(ps.stem(argv[1]))


if __name__ == '__main__':
    main()
