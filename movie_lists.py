# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:09:35 2023

@author: ethan.drover
"""

print("COMMAND MENU")
print("list - List all movies\nadd - Add a movie\ndel - Delete a movie\nexit - Exit program")
program = True

while program:
    movies = ['Monty python and the holy grail', 
              'On the waterfront', 'Cat on a tin roof',
              'Casablanca']
    
    command = input("\nCommand: ")
    
    if command == 'list':
            print(movies)
        
    elif command == 'add':
        name = input("Name: ")
        movies.append(name)
        print("{} Was added.".format(name))
    
    elif command == 'del':
        number = input("Number: ")
        movies.remove(number)
        print("{} Was removed.".format(number))
        
    elif command == 'exit':
        print("\nBye!")
        break

         
    
        
