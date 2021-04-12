#!/usr/bin/env python3

from bs4 import BeautifulSoup
import lxml
import requests
import re

mainUrl = 'http://www.gdacs.org/XML/RSS.xml'
resources = []

def makeSoup(url):
	resp = requests.get(url)
	soup = BeautifulSoup(resp.content, features="xml")
	
	return soup

def scrape():
	disasters = {}
	counter = 0
	items = makeSoup(mainUrl).findAll('item')
	for i in items:
		alert_level = i.find('alertlevel').text
		if alert_level == 'Red' or alert_level == 'Orange':
			resources.append(i.resources.findAll('resource'))
	impact_xmls = []
	impact_data = []
	for r in resources:
		for i in r:
			print(i['id'])
			if i['id'] == 'impact_xml':
				impact_xmls.append(i['url'])
			elif i['id'] == 'impact_data':
				impact_data.append(i['url'])
	xml_calculations = []
	xml_contentdata = []
	for xml in impact_xmls:
	  calc_match = re.search('calculation', xml)
	  if calc_match:
	    xml_calculations.append(xml)
	for site in xml_calculations:
	  datums = makeSoup(site).findAll('datums')
	  for d in datums:
	    if d['alias'] == 'City':
	      data = d.findAll('datum')
	      for i in data:
	        scalars = i.findAll('scalar')
	        for scalar in scalars:
	          name = scalar.find('name')
	          if name.text == 'NAME':
	            disaster = {}
	            counter += 1
	            disaster['city'] = scalar.value.text      
	          if name.text == 'COUNTRY':
	            disaster['country'] = scalar.value.text
	            disaster['type'] = datums.find('model-name').text
	            disasters[counter] = disaster
	for link in impact_data:
	  pre = makeSoup(link).findAll('a')
	  for a in pre:
	    if a.text == 'final':
	      url = 'http://webcritech.jrc.ec.europa.eu' + a['href'] + 'locations.xml'
	      items = makeSoup(url).findAll('item')
	      for item in items:
	        if item.cityName != None:
	          disaster = {}
	          counter += 1
	          disaster['city'] = item.cityName.text
	          disaster['country'] = item.country.text
	          disaster['type'] = items.title.text.lower()
	          disasters[counter] = disaster
	
	return disasters

def counts():
	totals = {}
	total_red = 0
	total_orange = 0
	total_green = 0
	items = makeSoup(mainUrl).findAll('item')
	for i in items:
		alert_level = i.find('alertlevel').text
		if alert_level == 'Red':
			resources.append(i.resources.findAll('resource'))
			total_red += 1
		elif alert_level == 'Orange':
			total_orange += 1
		elif alert_level == 'Green':
			total_green += 1
	totals['red'] = total_red
	totals['orange'] = total_orange
	totals['green'] = total_green

	return totals

