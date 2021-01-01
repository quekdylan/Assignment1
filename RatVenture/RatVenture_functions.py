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
            player = Entity("The Hero", int(data[0]), "2-4", 1)
            location, day = data[1], int(data[2])
            print("Save file found. Resuming game...")
    except IOError:
        print("Save file not found.")
        player, location, day = newGame(), "0,0", 1
    return(player, location, day)


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

def saveGame(health, location, day, full_path=None):

    #Path of current working directory
    #path = os.getcwd()
    if(full_path == None):
        full_path = (os.getcwd() + "\\" + "RatVenture" + "\\" + "save.txt")

    #Full path of savefile
    #full_path = (path + "\\" + "RatVenture" + "\\" +fileName)

    f = open(full_path, "w+")
    for s in [str(health), '\n', str(location), '\n', str(day)]:
        f.write(s)

def viewMap(location):
    # This function produces a map with the player's current location
    # Input: Player's coordinates
    # Output: Map (string)
    output = ""
    townCoordinates = ["0,0", "3,1", "5,2", "1,3", "4,6"]
    for y in range(17):
        if(y%2 == 0):
            output += ("+---+---+---+---+---+---+---+---+")
        else:
            for x in range(8):
                pointer = str(x) + "," + str(int((y-1)/2))
                if(pointer == location):
                    if(pointer in townCoordinates):
                        output+= "|H/T"
                    else:
                        output+= "| H "
                elif(pointer in townCoordinates):
                    output+= "| T "
                elif(pointer == "7,7"):
                    output+= "| K "
                else:
                    output += "|   "
            output += "|"
        output += "\n"
    return(output)

def move(location, direction, day):
    # This function updates the player location based on the direction, and adds a day 
    # Input: Player coordinates, direction, current day
    # Output: Updated location and day
    coordinates = list(map(int, location.split(",")))
    if(direction == "w" or direction == "W"):
        coordinates[1] -= 1
    elif(direction == "a" or direction == "A"):
        coordinates[0] -= 1
    elif(direction == "s" or direction == "S"):
        coordinates[1] += 1
    elif(direction == "d" or direction == "D"):
        coordinates[0] += 1
    else:
        print("Invalid input, please try again.")
        return(0)
    if(coordinates[0] >= 0 and coordinates[0] <= 7 and coordinates[1] >= 0 and coordinates[1] <= 7):
        updatedLocation = ','.join(map(str, coordinates))
        updatedDay = day + 1
        return(updatedLocation, updatedDay)
    else:
        print("Out of bounds, please try again.")
        return(0)

def checkLocation(coordinates):
    # This function checks if the player is in a town, outdoors or at the orb of power
    # Input: Player coordinates
    # Output: Player location

    townCoordinates = ["0,0", "3,1", "5,2", "1,3", "4,6"]
    orbCoordinates = "7,7"

    if (coordinates in townCoordinates):
        return("a town")
    elif (coordinates == orbCoordinates):
        return("the orb")
    else:
        return("the open")

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
