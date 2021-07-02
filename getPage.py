from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument('log-level=2')
driver = webdriver.Chrome(options=options)

import requests
import json
from bs4 import BeautifulSoup



def getPageSelenium(url):
	driver.get(url)
	result = driver.page_source
	return BeautifulSoup(result, 'html.parser')


def getPageRequests(url):
	return BeautifulSoup(requests.get(url).text, 'html.parser')


def finish():
	driver.close()