#!/usr/bin/env python3

from bs4 import BeautifulSoup
import lxml
import requests
import re

def scrape():

	resources = []
	disasters = {}
	counter = 0


	url = 'http://www.gdacs.org/XML/RSS.xml'
	resp = requests.get(url)
	soup = BeautifulSoup(resp.content, features="xml")
	items = soup.findAll('item')


	for i in items:
		alert_level = i.find('alertlevel').text

		if alert_level == 'Red':
			resources.append(i.resources.findAll('resource'))

	impact_xmls = []
	impact_data = []

	for r in resources:
	  for i in r:
	    if i['id'] == 'impact_xml':
	      impact_xmls.append(i['url'])
	    elif i['id'] == 'impact_data':
	      impact_data.append(i['url'])

	xml_calculations = []
	xml_contentdata = []



	for xml in impact_xmls:
	  calc_match = re.search('calculation', xml)
	  # data_match = re.search('contentdata', xml)
	  if calc_match:
	    xml_calculations.append(xml)
	  
	  # if data_match:
	  #   xml_contentdata.append(xml)


	for site in xml_calculations:
	  resp_3 = requests.get(site)
	  soup_3 = BeautifulSoup(resp_3.content, features="xml")
	  datums = soup_3.findAll('datums')
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
	            disaster['type'] = soup_3.find('model-name').text
	            disasters[counter] = disaster

	for link in impact_data:
	  resp_4 = requests.get(link)
	  soup_4 = BeautifulSoup(resp_4.content, 'lxml')
	  pre = soup_4.pre.findAll('a')
	  for a in pre:
	    if a.text == 'final':
	      url = 'http://webcritech.jrc.ec.europa.eu' + a['href'] + 'locations.xml'
	      resp_5 = requests.get(url)
	      soup_5 = BeautifulSoup(resp_5.content, features="xml")
	      items = soup_5.findAll('item')
	      for item in items:
	        if item.cityName != None:
	          disaster = {}
	          counter += 1
	          disaster['city'] = item.cityName.text
	          disaster['country'] = item.country.text
	          disaster['type'] = soup_5.title.text.lower()
	          disasters[counter] = disaster
	
	return disasters

def counts():

	totals = {}

	total_red = 0
	total_orange = 0
	total_green = 0

	url = 'http://www.gdacs.org/XML/RSS.xml'
	resp = requests.get(url)
	soup = BeautifulSoup(resp.content, features="xml")
	items = soup.findAll('item')


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

disasters = scrape()
counts = counts()