# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:49:01 2023

@author: ethan.drover
"""

import csv

def write_file(collection):
    with open("all_sales.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(collection) 


def read_file():
    sales_data = []
    with open('all_sales.csv', newline='') as file_handler:
        reader = csv.reader(file_handler)
        for row in reader:
            #print(f'{row[0]} :-) {row[1]}')
            sales_data.append(float[row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4])])
    return sales_data