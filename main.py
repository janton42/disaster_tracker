#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Jeff Stock"
__version__ = "0.1.0"
__license__ = "GNU GENERAL PUBLIC LICENSE"

from file_reader import us_based
from scraper import disasters
from comparison import affected

def main():
    """ Main entry point of the app """

    print(len(affected))
    print(affected)

    # print(disasters.get(10))

    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()