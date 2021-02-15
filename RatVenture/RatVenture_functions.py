import sys
import os
import re
import random
from pathlib import Path
from RatVenture_classes import *
import random


def mainMenu():
    """
    This function prints out the main menu
    @author Dong Han
    """
    print("Welcome to Ratventure!")
    print("----------------------")
    print("1) New Game")
    print("2) Resume Game")
    print("3) Exit Game")
    

def newGame():
    #This function creates and return a player object with default stats
    #Input: -
    #Output: "Starting new game..."
    #           Player object(Name, Health, Damage, Defence, Orb)

    print("Starting new game...\n")

    #init the player object
    player = Entity("The Hero", 20, "2-4", 1)
    return player

def resumeGame(filename):
    """
    This function reads any previous save files and loads it
    @param filename The name of the save file
    @author Dylan
    """
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
    """
    This function exits the game
    @author Dong Han
    """

    exit()

    print("Exit has failed.")


def townMenu(v_day):
    """
    This function prints out the town menu
    @param v_day Contains the value of the current day
    @author Dong Han
    """

    print(f"Day {v_day}. You are in a town.")
    print("1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Rest")
    print("5) Save Game")
    print("6) Exit Game")

def viewCharacter(player):
    """
    This function displays the player's statistics
    @param player The entity object of player
    @author Dong Han
    """

    print(player.name)
    print(f" Damage: {player.damage}")
    print(f"Defence: {player.defence}")
    print(f"    HP : {player.health}")

def rest(day, health):
    """
    This function restores the player's health to 20, and add 1 to day.
    @param day The current day value
    @param health The current health value
    @author Dong Han
    """

    day = day + 1
    health = 20

    print("You are fully healed.")    

    return day, health

def saveGame(health, location, day, full_path=None):
    """
    This function saves the game \n
    Output: filename.txt
    @param health Players' health
    @param location Current location of player
    @param day Current day
    @param fullpath Path of the saveFile
    @author Dong Han
    """

    #Path of current working directory
    #path = os.getcwd()
    if(full_path == None):
        full_path = (os.path.dirname(__file__)  + "\\" + "save.txt")
        print(full_path)

    #Full path of savefile
    #full_path = (path + "\\" + "RatVenture" + "\\" +fileName)

    f = open(full_path, "w+")
    for s in [str(health), '\n', str(location), '\n', str(day)]:
        f.write(s)

def viewMap(location, townCoordinates, orb_location, orb_found):
    """
    This function produces a map with the player's current location
    @param location Player's current location
    @param townCoordinates List of coordinates of towns
    @param orb_location Coordinates of orb
    @param orb_found Boolean if orb is found
    @author Dylan
    """
    output = ""
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
                    if(not orb_found and pointer == orb_location):
                        output+= "|T/O"
                    else:
                        output+= "| T "
                elif(pointer == "7,7"):
                    output+= "| K "
                else:
                    output += "|   "
            output += "|"
        output += "\n"
    return(output)

def move(location, direction, day):
    """
    This function updates the player location based on the direction, and adds a day 
    @param location Player's current location
    @param direction Input Direction (W,A,S,D)
    @param day Current day
    @author Dylan
    """
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

def checkLocation(coordinates, townCoordinates):
    """
    This function checks if the player is in a town, outdoors, at the orb of power or rat king
    @param coordinates Player's current location
    @param townCoordinates List of town coordinates
    @author Dylan, Dong Han
    """
    
    kingCoordinates = "7,7"

    if (coordinates in townCoordinates):
        return("You are in a town")
    elif (coordinates == kingCoordinates):
        return("You see the Rat King!")
    else:
        return("You are in the open")

def combatMenu(enemy):
    """
    This function displays the combat menu
    @param enemy Enemy object (Entity class)
    @author Dylan
    """
    print("\nEncounter! - " + enemy.name)
    print("Damage: " + enemy.damage)
    print("Defence: " + str(enemy.defence))
    print("HP: " + str(enemy.health)) 
    print("1) Attack\n2) Run")
    

def attack(player, enemy, orb=False):
    """
    This function is responsible for the attack mechanics in the game   \n
    Output: Player object, enemy object, status                         
    @param player The player object (Entity)
    @param enemy The enemy object (Entity)

    @return player The updated player object (Entity)
    @return enemy The updated enemy object (Entity)
    @return status The status of the battle

    @author Dong Han
    """

    #status 0 = Player wins
    #status 1 = Player loses
    #status 2 = Battle continues


    # 0 = unkillable
    # 1 = killable
    killable = checkKillable(enemy, orb)

    if(killable == 1):
        #Calculate player damage using player damage range - enemy defence
        playerDamage = pickRandomNumber(player.damage) - enemy.defence
        #Check if player damage is 0
        if(playerDamage < 0):
            playerDamage = 0
        enemy.health = enemy.health - playerDamage
        print(f"You deal {playerDamage} damage to the {enemy.name}")
    elif(killable == 0):
        # Rat king not killable
        print("Rat King has taken no damage! You need the orb of power!")
    #checks if enemy health is less than 0
    if(enemy.health <= 0):
        status = 0
    
    #if enemy health more than 0, battle continues
    else:
        #Calculate enemy damage using enemy damage range - player defence
        enemyDamage = pickRandomNumber(enemy.damage) - player.defence
        #Check if player damage is 0
        if(enemyDamage < 0):
            enemyDamage = 0
        player.health = player.health - enemyDamage
        print(f"Ouch! The {enemy.name} hit you for {enemyDamage} damage!")
        print(f"You have {player.health} HP left.")
        #checks if player health is less than 0 
        if (player.health <= 0):
            status = 1
    
    # If player health and enemy health both above 0, battle continues
    if(enemy.health > 0 and player.health > 0):
        status = 2
    return player, enemy, status


def pickRandomNumber(damage):
    """
    This function picks a random number from a string of numbers. 
    @param The damage values in string format. e.g.("2-5")
    @author Dong Han
    """
    #"2-4" - Removes the dash and adds the digit into list1
    list1 = [int(s) for s in damage.split("-") if s.isdigit()]
    #use range() to create a list of numbers using the 2 values in list1
    damageList = list(range(list1[0],list1[1]+1))
    #use random to pick a random number from damageList
    number = random.choice(damageList)
    return number


def outdoorMenu():
    """
    This function displays the outdoor menu
    @author Dylan
    """
    print("\n1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Exit Game")

def run():
    print("You run and hide")

def checkKillable(enemy, orb):
    """
    This function checks whether if the enemy is damageable
    @param enemy The enemy object (Entity)
    @param orb The orb object (bool)
    # Output: 0 - Enemy unkillable
    #         1 - Enemy killable
    @author Dong Han
    """

    # Check if enemy is Rat King
    if(enemy.name == "Rat King" and orb == True):
        return 1

    elif(enemy.name == "Rat King" and orb == False):
        return 0

    else:
        return 1

    
    """
    This function displays a message when the player runs
    @author Dylan
    """
    print("You run and hide")

def setOrbLocation(town_locations):
    """
    This function sets a location for the orb, that will be in a town that is not the starting town.
    @param town_locations List of town locations
    @author Dylan
    """
    locations = []
    for location in town_locations:
        if(location != "0,0"):
            locations.append(location)
    if locations == []:
        return NULL
    orb_location = random.choice(locations)
    return orb_location

def pickOrb(player):
    damage = player.damage.split('-')
    min_dmg = int(damage[0]) + 5
    max_dmg = int(damage[1]) + 5
    new_damage = str(min_dmg) + "-" + str(max_dmg)
    new_defence = player.defence + 5
    new_player = Entity("The Hero", player.health, new_damage, new_defence, True)

    print('You found the orb of power!')
    print('Your attack increases by 5!')
    print('Your defense increases by 5!')
    return new_player
