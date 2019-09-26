#!/usr/bin/env python3

from file_reader import fl_locations
from scraper import disasters

# scraper_test = {'city': 'Honitetoe', 'country': 'Indonesia', 'type': 'EQ'}

def generate_affected_list():
	
	affected_list = []
	
	for loc in fl_locations:
		for dis in disasters:
			affected = {}
			single_loc = fl_locations[loc]
			single_dis = disasters[dis]
			if single_loc['country'] == single_dis['country'] and single_loc['city'] == single_dis['city']:
				affected['uid'] = single_loc['uid']
				affected['fl_name'] = single_loc['fl_name']
				affected['country'] = single_loc['country']
				affected['city'] = single_loc['city']
				affected['type'] = single_dis['type']
				affected_list.append(affected)

	affected_list.append('End of List')

	return affected_list

generator = generate_affected_list()

		
