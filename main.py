#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Jeff Stock"
__version__ = "0.1.0"
__license__ = "GNU GENERAL PUBLIC LICENSE"

from file_reader import location_data_all, us_based

def main():
    """ Main entry point of the app """
    test = location_data_all.get(10)
    nation = test['country']
    print(nation)
    print(len(us_based))
    print(us_based[5])

    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()