# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:09:35 2023

@author: ethan.drover
"""
def menu():
    print("COMMAND MENU")
    print("list - List all movies\nadd - Add a movie\ndel - Delete a movie\nexit - Exit program")
program = True
movies = ['Monty python and the holy grail', 
           'On the waterfront', 'Cat on a tin roof',
           'Casablanca']
while program:
   
    
    command = input("\nCommand: ")
    
    if command.lower() == 'list':
        for i,movie in enumerate(movies, start=1):
            print('{}. {}'.format(i,movie))
        
    elif command.lower() == 'add':
        name = input("Name: ")
        movies.insert(0,name)
        print("{} Was added.".format(name))
    
    elif command.lower() == 'del':
        number = int(input("Number: "))
        if number < 1 or number > len(movies):
            print("Invalid Selection \n")
        else:
            movie = movies.pop(number-1)
        print("{} Was removed.".format(movie))
        
    elif command.lower() == 'exit':
        print("\nBye!")
        break


    

         
    
        
