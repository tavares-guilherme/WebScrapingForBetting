import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url = "https://www.soccerstats.com/"
driver = webdriver.Firefox()

driver.get(url)
time.sleep(5)           # Wait until page is loading
print("Page Loaded.")

driver.find_element_by_css_selector(".css-flk0bs").click() # Accepting Cookies Policy  
print("Cookies Accepted.")

brLeaguePath = "#headerlocal > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(5) > span:nth-child(1) > a:nth-child(1)"
driver.find_element_by_css_selector(brLeaguePath).click()

#!- Getting next matches table, to generate each match analysis URL -!#

# Interpreting HTML data
element = driver.find_element_by_css_selector(
        ".eight > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1)") # Select matches table
html_content = element.get_attribute('outerHTML')                                                                   
soup = BeautifulSoup(html_content,'html.parser')

# Getting href table
href_table_matches = []
count  = 0
for a in  soup.find_all("a", class_="vsmall"):
    href_table_matches.insert(count, a['href'])
    count = count + 1

# Generating URL table
url_table_matches = []
for i in range(0,count):
    url_table_matches.insert(i, url + href_table_matches[i])

print(url_table_matches[0])
print(url_table_matches[1])


#!- Getting each match statistics -!#
for i in range(0, count):
    driver.get(url_table_matches[i])
    time.sleep(1)
    driver.quit()

driver.quit()