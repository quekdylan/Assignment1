import sys
import os
import re
from pathlib import Path
from RatVenture_classes import *

def mainMenu():
    #This function prints out the main menu
    #Input: -
    #Output: -
    print("Welcome to Ratventure!")
    print("----------------------")
    print("1) New Game")
    print("2) Resume Game")
    print("3) Exit Game")

def newGame():
    #This function creates and return a player object with default stats
    #Input: -
    #Output: "Starting new game..."
    #           Player object(Name, Health, Damage, Defence)

    print("Starting new game...")

    #init the player object
    player = Entity("The Hero", 20, "2-4", 1)
    return player

def resumeGame(filename):
    # This function reads any previous save files and loads it
    # Input: save file name
    # Output: hp, location, day
    try:
        with open(filename, 'r') as f:
            data = f.read().split('\n')
            hp, location, day = int(data[0]), data[1], int(data[2])
            print("Save file found. Resuming game...")
    except IOError:
        print("Save file not found. ")
        hp, location, day = 20, "0,0", 1
    return(hp, location, day)


def exitGame():
    # This function exits the game
    # Input: -
    # Output: 

    try:
        sys.exit()

    except:
        print("Exit has failed.")


def townMenu(v_day):
    # This function prints out the town menu
    # Input: v_day: Contains the value of the current day
    # Output: -

    f"Day {v_day}. You are in a town."
    print("1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Rest")
    print("5) Save Game")
    print("6) Exit Game")

def viewCharacter(name, health, damage, defence):
    # This function displays the player's statistics
    # Input: name, health, damage, defence
    # Output: -

    print(name)
    f" Damage: {damage}"
    f"Defence: {defence}"
    f"    HP : {health}"

def rest(day, health):
    # This function restores the player's health to 20, and add 1 to day.
    # Input: Day, Health
    # Output: Day, Health

    day = day + 1
    health = 20

    print("You are fully healed.")    

    return day, health

def saveGame(health, location, day, fileName="save.txt"):

    #Path of current working directory
    path = os.getcwd()
    
    #Full path of savefile
    full_path = (path + "\\" + "RatVenture" + "\\" +fileName)

    with open(full_path, 'w') as f:
        for s in [str(health), '\n', str(location), '\n', str(day)]:
            f.write(s)


def combatMenu():
    print("a")

def outdoorMenu():
    print("a")

def checkTown():
    #This function checks whether if the player is in town or not
    #Input: location: Current location of player
    #Returns: True if in town, False if not
    print("a")

def checkEncounter():
    #This function checks whether if the player encounters a monster
    #Input: ?
    #Output: True if encounters monster, false if not
    print("a")
