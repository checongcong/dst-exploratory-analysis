# Usage:
#   python main.py --data="../data/IAGA-2000.txt"

from __future__ import absolute_import, division, print_function

import argparse

from dst import Dst
from parser_iaga import IAGAParser

def argparser():
    """Parses command line options and returns an args object"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default=None,
                        help="Specify a data file as an argument")
    return parser

def main():
    parser = argparser()
    args = parser.parse_args()
    if not args.data:
        return parser.print_help()
    
    iaga_parser = IAGAParser()
    dst = iaga_parser.parse_file(args.data)
    dst.head(5)

if __name__ == '__main__':
    main()