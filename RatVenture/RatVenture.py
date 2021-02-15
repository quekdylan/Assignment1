from RatVenture_functions import *
from RatVenture_classes import *
import sys

#Default values
v_filename = "save.txt"
v_location="0,0"
v_day = 1
v_rat_encounter = False
v_town_locations = ["0,0", "3,1", "5,2", "1,3", "4,6"]
v_orb_location = setOrbLocation(v_town_locations)

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

#Main program    
while(True):
    # If player is in a town
    if(checkLocation(v_location, v_town_locations) == "a town"):
        # If orb in town
        if (v_location == v_orb_location):
            player = pickOrb(player)
            
        townMenu(v_day)
        choice = int(input("Enter your choice: "))
        # View Character
        if(choice == 1):
            viewCharacter(player)
            continue

        # View Map
        elif(choice == 2):
            print(viewMap(v_location, v_town_locations, v_orb_location, player.orb))
            continue

        # Move 
        elif(choice == 3):
            while(True):
                print(viewMap(v_location, v_town_locations, v_orb_location, player.orb))
                print("W = up; A = left; S = down; D = right")
                direction = input("Your Move: ")
                if(move(v_location, direction, v_day) != 0):
                    v_location, v_day = move(v_location, direction, v_day)
                    print(viewMap(v_location, v_town_locations, v_orb_location, player.orb))
                    print("Day " + str(v_day) + ". You are in " + checkLocation(v_location, v_town_locations))
                    break

        # Rest
        elif(choice == 4):
            v_day, player.health = rest(v_day, player.health)
            continue

        # Save Game
        elif(choice == 5):
            saveGame(player.health, v_location, v_day)
            continue

        # Exit Game
        elif(choice == 6):
            exitGame()

        #User inputs invalid option
        else:
            print("Invalid option")
            continue
    
    # Rat encounter
    elif(checkLocation(v_location, v_town_locations) == "the open" and v_rat_encounter == False):
        enemy = Entity('Rat', 10, '1-3', 1)
        in_combat = True
        while(in_combat):
            combatMenu(enemy)
            combatChoice = input("Enter Choice: ")

            # Attack
            if(combatChoice == '1'):
                player, enemy, status = attack(player, enemy)
                if(status == 2):
                    continue
                elif(status == 0):
                    print('The rat is dead! You are victorious!')
                    in_combat = False
                    v_rat_encounter = True
                elif(status == 1):
                    print('You died. Game over.')
                    exitGame()
            # Run
            elif(combatChoice == '2'):
                run()
                outdoorMenu()
                outdoorChoice = input("Enter choice: ")

                # View Character
                if(outdoorChoice == '1'):
                    viewCharacter(player)
                    # Rat encounter (Health is reset)
                    enemy = Entity('Rat', 10, '1-3', 1)

                # View Map
                elif(outdoorChoice == '2'):
                    print(viewMap(v_location, v_town_locations, v_orb_location, player.orb))
                    # Rat encounter (Health is reset)
                    enemy = Entity('Rat', 10, '1-3', 1)

                # Move
                elif(outdoorChoice == '3'):
                    in_combat = False
                    while(True):
                        print(viewMap(v_location, v_town_locations, v_orb_location, player.orb))
                        print("W = up; A = left; S = down; D = right")
                        direction = input("Your Move: ")
                        if(move(v_location, direction, v_day) != 0):
                            v_loca1tion, v_day = move(v_location, direction, v_day)
                            print(viewMap(v_location, v_town_locations, v_orb_location, player.orb))
                            print("Day " + str(v_day) + ". You are in " + checkLocation(v_location, v_town_locations))
                            break

                # Exit Game
                elif(outdoorChoice == '4'):
                    exitGame()
                else:
                    print("Invalid option. Please try again.")
            else:
                print("Invalid option. Please try again.")
        continue

    # If player is in the open and has already encountered a rat
    elif(checkLocation(v_location, v_town_locations) == "the open"):
        outdoorMenu()
        outdoorChoice = input("Enter choice: ")

        # View Character
        if(outdoorChoice == '1'):
            viewCharacter(player)

        # View Map
        elif(outdoorChoice == '2'):
            print(viewMap(v_location, v_town_locations, v_orb_location, player.orb))

        # Move
        elif(outdoorChoice == '3'):
            while(True):
                print(viewMap(v_location, v_town_locations, v_orb_location, player.orb))
                print("W = up; A = left; S = down; D = right")
                direction = input("Your Move: ")
                if(move(v_location, direction, v_day) != 0):
                    v_location, v_day = move(v_location, direction, v_day)
                    print(viewMap(v_location, v_town_locations, v_orb_location, player.orb))
                    print("Day " + str(v_day) + ". You are in " + checkLocation(v_location, v_town_locations))
                    break

        # Exit Game
        elif(outdoorChoice == '4'):
            exitGame()
        else:
            print("Invalid option. Please try again.")