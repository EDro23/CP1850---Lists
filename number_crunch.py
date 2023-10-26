# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 09:17:26 2023

@author: ethan.drover
"""
# import random

   # rand_data = random.randint(range, 1,50)
   # avg_rand = ((sum),rand_data)

tuple_data = (0,5,10,15,20,25,30,35,40,45,50)
totalsum = (sum(tuple_data))
avg = totalsum/len(tuple_data)
min_num = min(tuple_data)
max_num = max(tuple_data)

sorted_data = sorted(tuple_data)
n = len(sorted_data) // 2
if len(sorted_data) % 2 == 0:
    median = (sorted_data[n - 1] + sorted_data[n]) / 2
else:
     median = sorted_data(n)
           
print("fTuple Data = {tuple_data}")
print("fAverage = {avg}")
print("fMedian = {median}")
print("fMin = {min_num}")
print("fMax = {max_value}")
print("fDuplicates = ")