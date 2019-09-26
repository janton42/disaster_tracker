#!/usr/bin/env python3

import csv

# def test(arg):
# 	print(f'arg = {arg}')

# thing = test("Hello World!")
location_data_all = {}
loc_data_counter = 0

us_based = []

contracts_list = csv.reader(open('./static/contracts.csv', 'r'))
contracts = {}
key = 0
for v in contracts_list:
   contracts[key] = v
   key += 1



for c in contracts:
	contract = {}
	loc_data_counter += 1
	
	location = contracts.get(c)[6]
	loc_list = location.split(',')

	contract['country'] = loc_list[0]
	contract['city'] = loc_list[-1].strip()

	
	uid = contracts.get(c)[4]
	fl_name = contracts.get(c)[5]

	contract['uid'] = uid
	contract['fl_name'] = fl_name

	location_data_all[loc_data_counter] = contract

for i in location_data_all:
	single_loc = location_data_all[i]
	nation = single_loc['country']
	if nation == 'United States':
		us_based.append(single_loc)





# countries_list = csv.reader(open('/Users/jeffstock/Desktop/Disaster/countries.csv', 'r'))
# countries = {}
# for k, v in countries_list:
#   countries[k] = v