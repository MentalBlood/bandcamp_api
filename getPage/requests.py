import requests

from bs4 import BeautifulSoup



def getPage(url):
	return BeautifulSoup(requests.get(url).text, 'html.parser')

paralleling = True