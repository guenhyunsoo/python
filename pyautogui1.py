# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:43:53 2020

@author: Administrator
"""


import pyautogui
import time
#pyautogui.moveTo(40, 54, 2)

#pyautogui.click(clicks=2, interval=2)

pyautogui.moveTo(1179, 116, 1)

pyautogui.doubleClick()

time.sleep(1)

#pyautogui.typewrite('Hello')
#pyautogui.typewrite(['enter'])
#pyautogui.typewrite(['a','b','c','enter'])
pyautogui.typewrite(['abc','enter'])