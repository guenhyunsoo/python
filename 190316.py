# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:54:45 2020

@author: Administrator
"""


numList = [100, 43, 21, 7, 98]
strList = ['blue', 'yellow', 'red', 'green', 'Black', 'Orange']

#numList.sort()
#print(numList)

#numList.reverse()
#print(numList)

#numList.sort(reverse=True)
#print(numList)

#strList.sort()
#print(strList)

#strList.sort(reverse=True)
#print(strList)

#strList.sort(key=str.lower)
#print(strList)

#numList2 = sorted(numList)
#numList2 = sorted(numList, reverse=True)
#print(numList)
#print(numList2)

#strList2 = sorted(strList, reverse=True)
strList2 = sorted(strList, reverse=True, key=str.lower)
print(strList)
print(strList2)

#numList2 = numList.sort()
#print(numList2)
