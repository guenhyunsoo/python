# selection sort by hwlee

import random

import time

a=[]

for i in range(3000):

    a.append(random.randint(1,1000))

b=[]

for i in range(3000):

    b.append(random.randint(1,1000))

def solve(a): # 새로운 리스트를 하나 만들어서 정렬

    b=[]

    for i in range(len(a)): # while a:

        index=solve1_index(a)

        b.append(a[index])

        a.pop(index)

    return b

        

def solve1_index(a):

    min_index=0

    for i in range(len(a)):

        if a[min_index] > a[i]:

            min_index=i

    return min_index

def solve2(a): # a라는 리스트에서 자리 바꿈으로 정렬

    for i in range(0, len(a)-1):

        min=a[i]

        index=i

        for j in range(i+1, len(a)):

            if min > a[j]:

                min=a[j]

                index=j

        a[i], a[index] = a[index], a[i]

    return a

start_time=time.time()

print (solve2(b))

process_time = time.time()-start_time

print (process_time)
