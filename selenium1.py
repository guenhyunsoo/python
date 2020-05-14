# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:30:48 2020

@author: Administrator
"""


from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
url = 'https://google.com'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

driver.find_element_by_css_selector('#gb_70').click()

time.sleep(2)
action.send_keys('guenhs').perform()
driver.find_element_by_css_selector('.CwaK9').click()

time.sleep(2)
driver.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys('ghs5738!@#')
driver.find_element_by_css_selector('.CwaK9').click()
