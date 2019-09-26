#!/usr/bin/env python3

from comparison import generator

def create_action_list():
	if len(generator) > 1:
	    with open('./static/affected.csv', 'w') as csvFile:
	        writer = csv.writer(csvFile)
	        writer.writerows(generator)