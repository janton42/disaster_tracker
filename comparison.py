#!/usr/bin/env python3

from file_reader import location_data_all as location

scraper_test = {'city': 'Honitetoe', 'country': 'Indonesia', 'type': 'EQ'}

affected_list = []

for loc in location:
	affected = {}
	single_loc = location[loc]
	if single_loc['country'] == scraper_test['country'] and single_loc['city'] == scraper_test['city']:
		affected['uid'] = single_loc['uid']
		affected['name'] = single_loc['name']
		affected['country'] = single_loc['country']
		affected['city'] = single_loc['city']
		affected['type'] = single_loc['type']
		affected_list.append(affected)


		
