# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 09:13:57 2023

@author: ethan.drover
"""

num_list = [1,5,6,8,9,45,78,45,17,25,65,5,5,5,5,5]
num_list.count(5)

fruits = ['apple', 'apple','apple','apple','apple','oranges','grapes']
fruits.count('apple')

num_list.reverse()
print(num_list)

num_list.sort()
num_list

fruits.sort()
print(fruits[1][0], num_list[0])
print(fruits[1][1], num_list[1])
print(fruits[1][2], num_list[2])
print(fruits[1][3], num_list[3])
print(fruits[1][4], num_list[4])

fruits.sort()
fruits
fruits.sort(key=str.upper)
sorted(fruits)
sorted(fruits, key=str.upper)
max(num_list)
sum(num_list)
sum(num_list, start=200)
