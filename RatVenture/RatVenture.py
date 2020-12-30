from RatVenture_functions import *
import sys

#Default values
v_name = "The Hero"
v_damage = "2-4"
v_defence = 1
v_hp = 20
v_location="0,0"
v_day = 1

#Display Main Menu 
mainMenu()
option = int(input("Enter your option: "))
if(option == 1):
    #newGame()
    print("1")


elif(option == 2):
    #resumeGame()
    print("2")

elif(option == 3):
    print("The game will now exit.")
    quit()

    
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

    

