#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Jeff Stock"
__version__ = "0.1.0"
__license__ = "GNU GENERAL PUBLIC LICENSE"


from scraper import counts
from datetime import datetime
from file_writer import create_action_list
from comparison import generate_affected_list
# from emailer import send_email

def main():
    """ Main entry point of the app """
    count_list = counts()
    red = count_list['red']
    orange = count_list['orange']
    green = count_list['green']
    
    now = datetime.now()
    date = now.strftime("%Y/%m/%d")
    time = now.strftime("%H:%M:%S")

    affected = generate_affected_list()
    if red == 0:
        print()
        print('No alert level "Red" disasters recorded.\n')
        create_action_list(affected)
    elif len(affected) == 1:
        print()
        print('There are no TIP freelancers affected by alert level "Red" natural disasters.\n', affected)
    else:
        print()
        print('Number of TIP freelancers possibly affected by a alert level "Red" natural disaster: ', len(affected))
        create_action_list(affected)
    	
    if red > 0:
    	print('Total Red alerts:', red, '\n')
    print('Total Orange alerts: ', orange, '\n')
    print('Total Green alerts: ', green,'\n')

    print('Search conducted date: ', date, '\n')
    print('Search conductad time: ', time, '\n')

    subject = 'Disaster Tracker ' + date
    body = 'Total Red alerts: ' + repr(red) + '\n' + '\n' + 'Total Orange alerts: ' + repr(orange) + '\n' + '\n' + 'Total Green alerts: ' + repr(green) + '\n' + '\n' + 'Search date ' + repr(date) + '\n' + '\n' + 'Search time' + repr(time)

    print(body)
    # send_email(subject, body)




if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()