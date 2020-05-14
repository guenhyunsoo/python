# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:08:38 2020

@author: Administrator
"""

#print('Hello'.rjust(20))
#print('Hello'.rjust(20, '-'))
#print('Hello'.ljust(20, '-'))
#print('Hello'.center(20, '-'))

fruit = {'apple':5, 'banana':8, 'grape':7, 'orange':3, 'peach':10}

for k, v in fruit.items():
    print(k.ljust(15, '-') + str(v).rjust(5))