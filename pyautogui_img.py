# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:14:34 2020

@author: Administrator
"""

import pyautogui

#print(pyautogui.position())

#pyautogui.moveTo(284, 143)
#pyautogui.click(284, 143)

i = pyautogui.locateOnScreen('7.png')
print(i)
