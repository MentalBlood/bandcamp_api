from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup



options = Options()
options.headless = True
options.add_argument('log-level=2')
driver = webdriver.Chrome(options=options)


def getPage(url):
	driver.get(url)
	result = driver.page_source
	return BeautifulSoup(result, 'html.parser')


atexit(driver.close)

paralleling = False