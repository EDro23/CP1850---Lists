# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 09:46:59 2023

@author: ethan.drover
"""

def menu_title():
    print(60 * "=")
    print("\t\t\t\tBaseball Team Manager")
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print("\nPOSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print(60 * "=")

def player_lineup():
    players = [['joe','P',]]


def display_lineup():
    menu_option = input("Menu Option: ")
    
    if menu_option == '1':
        print("\t\tPlayer\t\t\t\tPOS\t\tAB\t\tH\t\tAVG")
        print(60*"-")
        
menu_title()
display_lineup()

        