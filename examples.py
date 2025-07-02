#!/usr/bin/env python3

# examples.py
"""
Example use of argparser module

Usage:
    python3 examples.py -f "foo" -b "bar"

Demo:
    python3 examples.py --demo

Show this message:
    python3 examples.py --help
"""
from parsers.argparser import argparser

def _demo():
    print(f"\N{goat}")

if __name__ == "__main__":
    argparser(help=__doc__, demo=_demo)
