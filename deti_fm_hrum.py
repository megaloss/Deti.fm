import time
import csv
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = '/home/yurick/anaconda3/envs/scraping/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get("https://www.deti.fm/fairy_tales")
search = driver.find_element_by_class_name("search__link.noajax")
search.click()
search = driver.find_element_by_class_name("search__input")
search.send_keys("Филина", Keys.RETURN)
driver.implicitly_wait(5)
results = driver.find_elements_by_class_name("search-result__link")
results[-1].click()
driver.implicitly_wait(2)
driver.switch_to.window(driver.window_handles[-1])

while (driver.find_element_by_id("btn-load__podcast").is_displayed()):
	driver.find_element_by_id("btn-load__podcast").click()
	time.sleep(0.3)

podcasts = driver.find_elements_by_class_name("podcasts__item-img")

names=driver.find_elements_by_class_name("podcasts__item-pic")

attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', podcasts[0])
#print (attrs)
csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'link'])
for index,podcast in enumerate(podcasts):

	source = requests.get('https://deti.fm'+ podcast.get_attribute("onclick").split(";")[1].split("'")[1]).text
	soup = BeautifulSoup(source, 'lxml')
	print(names[index].get_attribute("title")+":")
	print (soup.find_all("audio")[1]["src"])
	csv_writer.writerow([names[index].get_attribute("title"), soup.find_all("audio")[1]["src"]])


driver.quit()
csv_file.close()
