from RatVenture_functions import *
from RatVenture_classes import *
import sys

#Default values
v_filename = "save.txt"

v_location="0,0"
v_day = 1

#Display Main Menu 
while(True):
    mainMenu()
    option = int(input("Enter your option: "))
    if(option == 1):
        #Creates a new game using newGame() function and receives player object
        player = newGame()
        break

    elif(option == 2):
        v_hp, v_location, v_day = resumeGame(v_filename)
        break

    elif(option == 3):
        print("The game will now exit.")
        exitGame()
    else:
        print("Invalid option. Please enter again.")

    
while(True):
    if(checkTown() == True):
        townMenu()
        choice = int(input("Enter your choice: "))
    elif(checkEncounter() == True):
        combatMenu()
        choice = int(input("Enter your choice: "))
    else:
        outdoorMenu()
        choice = int(input("Enter your choice: "))
