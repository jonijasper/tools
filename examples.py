#!/usr/bin/env python3

# examples.py
"""
Example use of argparser and spread module

Usage:
    python3 examples.py -f foobar -b 1 2 3

Demo:
    python3 examples.py --demo

Show this message:
    python3 examples.py --help
"""
import pandas as pd 

from parsers.argparser import argparser
from helpers import sheetwriters


def _demo():
    print(f"\N{goat}")

def spreadsheet_example(file: str, values: list):
    df = pd.DataFrame({ "foo": ["a", "b", "c"], 
                        "bar": values, 
                        "sheet": ["Sheet1", "Sheet1", "Sheet2"]})
                        
    sheetwriters.spread(df, f"{file}.xlsx", key="sheet", engine="xlsxwriter")

if __name__ == "__main__":
    args = argparser(help=__doc__, demo=_demo)
    spreadsheet_example(*args)
