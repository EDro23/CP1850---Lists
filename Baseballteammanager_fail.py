#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:14:29 2023

@author: kaileyslaney
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
    
def display_lineup(players):
    for i,players in enumerate (players, start=1):
        print("{}\t\t{}\t\t\t{}\t\t{}\t\t{}".format(i,players[0],players[1],players[2],players[3]))
        print()
        
   

def player_add(players):
            name = input("Name: ")
            position = input("Position: ")
            hits = input("Hits: ")
            at_bats = input("At Bats: ")
            avg = (hits/at_bats)
            players.append(name,position,hits,at_bats,avg)
            print("{} Was added.".format(name))

    
def main():
    players = [['joe','tom','ben','mike'],['P','SS','3B','C'],['10','11','9','4'],['2','4','3','1']]
    menu_title()
    while True:
        menu_option = input("Menu Option: ")
    if menu_option == '2':
        player_add(players)
    else:
        print("Invalid command")
        

main()