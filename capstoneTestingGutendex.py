# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 12:29:21 2022

@author: adfis
"""

 # https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08
from selenium import webdriver
from time import sleep

path = "C:\\Users\\adfis\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://gutendex.com/')

id_box = driver.find_element_by_id('ax-url')
id_box.send_keys('?topic=monster')

search_click = driver.find_element_by_class_name('btn-primary')
search_click.click()

sleep(15)

output_text = driver.find_element_by_id('ax-results')
stringofresults = output_text.text
print(stringofresults)# i now have a full string of all the stuff, need to search for txt