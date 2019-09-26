#!/usr/bin/env python3

def create_action_list(generator):

	if len(generator) > 1:
	    with open('./static/affected.csv', 'w') as csvFile:
	        writer = csv.writer(csvFile)
	        writer.writerows(generator)