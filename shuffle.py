# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:59:20 2020

@author: Administrator
"""


import random

i = list(range(10))
#q = i[:]

#print(i)

#random.shuffle(i)
#random.shuffle(q)

q = random.sample(i,10)

print(i)
print(q)