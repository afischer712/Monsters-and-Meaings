# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:10:32 2022

@author: adfis
"""


 # https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08
from selenium import webdriver
from time import sleep

path = "C:\\Users\\adfis\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://www.dndbeyond.com/monsters?filter-type=0&filter-search=&filter-cr-min=&filter-cr-max=&filter-armor-class-min=&filter-armor-class-max=&filter-average-hp-min=&filter-average-hp-max=&filter-is-legendary=&filter-is-mythic=&filter-has-lair=&filter-source=1')

id_box = driver.find_element_by_id('a')#cant find, trying to click link to monster stat page
id_box.click()#if you can get it to type things, you can get it to ctrl A
#finding the links to each monster page will be hard, but I COULD decide that it would be best to input a url to work with

