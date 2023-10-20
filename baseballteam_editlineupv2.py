# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 08:30:25 2023

@author: ethan.drover
"""

POSITIONS = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P']

def seperator():
    print(60 * "=")
    
def title():
    print("\t\t\t\tBaseball Team Manager")
    
def menu_title():
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
        print("{}\t\t{}\t\t{}\t\t\t{:.2f}\t\t\t{:.2f}\t\t\t{:.2f}".format(i,players[0],players[1],players[2],players[3],(players[2]/players[3])))
        print()
        
   

def player_add(players):
            name = str(input("Name: "))
            position = str(input("Position: "))
            hits = int(input("Hits: "))
            at_bats = int(input("At Bats: "))
            players.append([name,position,hits,at_bats])
            print("{} Was added.".format(name))
            
def display_pos():
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
            
def remove_player(players):
    remove_plyr = int(input("Player: "))
    name = players.pop(remove_plyr-1)
    print("{} Has been removed".format(name[0]))

def get_pos(players):
    while True:
        position = input("Position: ").upper()
        if position in POSITIONS:
            return position
        else:
            print("Invalid position. Try again.")
            display_pos()

def at_bats():
    while True:
        

    
def main():
    players = [['joe ','P',10,2],['Tom ','SS',11,4],['Ben ','3B',9,3],['Mike','C',4,1]]
    seperator()
    title()
    seperator()
    menu_title()
    while True:
        menu_option = input("Menu Option: ")
        if menu_option == '1':
            print("\t\tPlayers\t\tPos\t\t\tBats\t\tHits\t\tAvg")
            print(60*"-")
            display_lineup(players)
        elif menu_option == '2':
            player_add(players)
        elif menu_option == '3':
            remove_player(players)
        elif menu_option == '7':
            print("Bye!")
            break
        else:
            print("Invalid command")
    print("Bye!")
        

if __name__ == '__main__':
    main()