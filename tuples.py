# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 09:01:09 2023

@author: ethan.drover
"""

# Creating tuples
# Syntax tuple_name = (item1, item2, item3,....)

hits = (48.0,30.0,20.2,100.0)
fruits = ('Apple', 'Orange', 'Banana', 'Kiwi', 'Grapes')
car = ('Honda','Civic',2012,46.8)

# Accessing elements

fruits[3]
car[1]

# car[1] = 'Golf' This will not add because its a tuple.

# Unpacking a tuple
mik, joe, ray, kia = hits

def tuple_example_fn():
    return 'Aru', 'Inst', 2023

name, pos, year = tuple_example_fn()
test1 = tuple_example_fn()
test1[1][0] = 'Racer'
