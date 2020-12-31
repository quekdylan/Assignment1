import sys

def mainMenu():
    #This function 
    print("Welcome to Ratventure!")
    print("----------------------")
    print("1) New Game")
    print("2) Resume Game")
    print("3) Exit Game")

def newGame():

    print("Starting new game...")

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

def townMenu():
    print("a")

def combatMenu():
    print("a")

def outdoorMenu():
    print("a")

def checkTown():
    #This function checks whether if the player is in town or not
    #input: location
    #returns: True if in town, False if not
    print("a")
