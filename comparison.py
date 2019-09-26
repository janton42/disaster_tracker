#!/usr/bin/env python3

from file_reader import location_compiler
from scraper import scrape

# scraper_test = {'city': 'Honitetoe', 'country': 'Indonesia', 'type': 'EQ'}

def generate_affected_list():
	
	affected_list = []
	fl_locations = location_compiler()
	disaster_list = scrape()
	
	for location in fl_locations:
		for disaster in disaster_list:
			affected = {}
			single_loc = fl_locations[location]
			single_dis = disaster_list[disaster]
			if single_loc['country'] == single_dis['country'] and single_loc['city'] == single_dis['city']:
				affected['uid'] = single_loc['uid']
				affected['fl_name'] = single_loc['fl_name']
				affected['country'] = single_loc['country']
				affected['city'] = single_loc['city']
				affected['type'] = single_dis['type']
				affected_list.append(affected)

	affected_list.append('List is Empty')

	return affected_list

		
