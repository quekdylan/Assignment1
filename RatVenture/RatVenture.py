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
        player, v_location, v_day = resumeGame(v_filename)
        break

    elif(option == 3):
        print("The game will now exit.")
        exitGame()
    else:
        print("Invalid option. Please enter again.")

    
while(True):
    if(checkLocation(v_location) == "a town"):
        townMenu(v_day)
        choice = int(input("Enter your choice: "))
        if(choice == 1):
            viewCharacter()
            continue

        elif(choice == 2):
            print(viewMap(v_location))
            continue

        elif(choice == 3):
            while(True):
                print(viewMap(v_location))
                print("W = up; A = left; S = down; D = right")
                direction = input("Your Move: ")
                if(move(v_location, direction, v_day) != 0):
                    v_location, day = move(v_location, direction, v_day)
                    print(viewMap(v_location))
                    print("Day " + str(v_day) + ". You are in " + checkLocation(v_location))
                    break

        elif(choice == 4):
            player.health, v_day = rest(player.health, v_day)
            continue
        elif(choice == 5):
            saveGame(player.health, v_location, v_day)
            continue
        elif(choice == 6):
            exitGame()
        else:
            print("Invalid option")
            continue
    
    elif(checkLocation(v_location) == "the open"):
        print("Sprint 3")
