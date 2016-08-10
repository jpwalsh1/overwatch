#!/usr/bin/python
# coding: utf8

import requests, bs4

# Script Settings
region = 'us'
platform = 'pc'
###

# Proxy settings if needed
proxies = {'http': '', 'https': '',}


# Team of players to lookup their ratings
team = ["Nicarras#1104" ]


def getRating(name):
	urlName = name.replace('#','-')
	url = "https://playoverwatch.com/en-us/career/" + platform + "/" + region +"/" + urlName
	response = requests.get(url, proxies=proxies, verify=False)
	soup = bs4.BeautifulSoup(response.text, 'html.parser')
	rating = soup.find('div', {'class': 'competitive-rank'}).find('div')
	print "{0:20}: {1}".format(name.split("#")[0], rating.text)

for char in team:
	getRating(char)
