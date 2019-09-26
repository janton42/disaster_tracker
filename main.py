#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Jeff Stock"
__version__ = "0.1.0"
__license__ = "GNU GENERAL PUBLIC LICENSE"


from comparison import generator
from scraper import counts

def main():
    """ Main entry point of the app """
    red = counts['red']
    orange = counts['orange']
    green = counts['green']

    if red == 0:
    	print('No alert level "Red" disasters recorded.')
    elif len(affected) == 0:
    	print('There are no TIP freelancers affected by alert level "Red" natural disasters.')
    else:
    	print('Number of TIP freelancers possibly affected by a alert level "Red" natural disaster')
    	print(len(generator))

    print("Total Red alerts:")
    print(red)
    print("Total Orange alerts:")
    print(orange)
    print("Total Green alerts:")
    print(green)


    # print(disasters.get(10))

    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()