"""
Example usage of argparser module

Show this message:
$ python3 examples.py --help

Run demo:
$ python3 examples.py --demo

Run with arguments:
$ python3 examples.py -f "foo" -b "bar"
"""
from parsers.argparser import argparser

def _demo():
    print(f"\N{goat}")

if __name__ == "__main__":
    argparser(help=__doc__, demo=_demo)