# Python Documentation

## Classes

**[Entity](Entity.md)**: This is a class of entities e.g.(Player, Rat, Rat King)   
Input: Name, Health, Damage, Defence, Orb=False   
Output:  Creates a object   
  
  
Example of how to initialize a entity   
player = Entity('The Hero', 20, "2-4", 1)   
print(player.health)   
  
Example of how to update variable in class   
player.health = (player.health - 1)   
print(player.health)   
  



## Functions

### test_combat







### testWin







### testLose







### test_rest



#### Parameters
name | description | default
--- | --- | ---
hp |  | 
day |  | 
resultHp |  | 
resultDay |  | 





### test_view_map_town







### test_view_map_outdoors







### test_saveGame



#### Parameters
name | description | default
--- | --- | ---
health |  | 
location |  | 
day |  | 
fullpath |  | 
resultHealth |  | 
resultLocation |  | 
resultDay |  | 





### test_resume_without_save







### mainMenu
Authors: **Dong Han**

This function prints out the main menu 




### newGame







### resumeGame
Authors: **Dylan**

This function reads any previous save files and loads it 
#### Parameters
name | description | default
--- | --- | ---
filename | The name of the save file | 





### exitGame
Authors: **Dong Han**

This function exits the game 




### townMenu
Authors: **Dong Han**

This function prints out the town menu 
#### Parameters
name | description | default
--- | --- | ---
v_day | Contains the value of the current day | 





### viewCharacter
Authors: **Dong Han**

This function displays the player's statistics 
#### Parameters
name | description | default
--- | --- | ---
player | The entity object of player | 





### rest
Authors: **Dong Han**

This function restores the player's health to 20, and add 1 to day. 
#### Parameters
name | description | default
--- | --- | ---
day | The current day value | 
health | The current health value | 





### saveGame
Authors: **Dong Han**

This function saves the game   
Output: filename.txt 
#### Parameters
name | description | default
--- | --- | ---
health | Players' health | 
location | Current location of player | 
day | Current day | 
full_path | Path of the saveFile | None





### viewMap
Authors: **Dylan**

This function produces a map with the player's current location 
#### Parameters
name | description | default
--- | --- | ---
location | Player's current location | 
townCoordinates | List of coordinates of towns | 
orb_location | Coordinates of orb | 
orb_found | Boolean if orb is found | 





### move
Authors: **Dylan**

This function updates the player location based on the direction, and adds a day 
#### Parameters
name | description | default
--- | --- | ---
location | Player's current location | 
direction | Input Direction (W,A,S,D) | 
day | Current day | 





### checkLocation
Authors: **Dylan, Dong Han**

This function checks if the player is in a town, outdoors, at the orb of power or rat king 
#### Parameters
name | description | default
--- | --- | ---
coordinates | Player's current location | 
townCoordinates | List of town coordinates | 





### combatMenu
Authors: **Dylan**

This function displays the combat menu 
#### Parameters
name | description | default
--- | --- | ---
enemy | Enemy object (Entity class) | 





### attack
Authors: **Dong Han**

This function is responsible for the attack mechanics in the game   
Output: Player object, enemy object, status 
#### Parameters
name | description | default
--- | --- | ---
player | The player object (Entity) | 
enemy | The enemy object (Entity) | 
orb | The orb value of player (bool) | False





### pickRandomNumber
Authors: **Dong Han**

This function picks a random number from a string of numbers. 
#### Parameters
name | description | default
--- | --- | ---
damage | The damage values in string format. e.g.("2-5") | 





### outdoorMenu
Authors: **Dylan**

This function displays the outdoor menu 




### run







### checkKillable
Authors: **Dong Han**

This function checks whether if the enemy is damageable 
#### Parameters
name | description | default
--- | --- | ---
enemy | The enemy object (Entity) | 
orb | The orb object (bool) # Output: 0 - Enemy unkillable #         1 - Enemy killable | 





### setOrbLocation
Authors: **Dylan**

This function sets a location for the orb, that will be in a town that is not the starting town. 
#### Parameters
name | description | default
--- | --- | ---
town_locations | List of town locations | 





### pickOrb



#### Parameters
name | description | default
--- | --- | ---
player |  | 





### checkoriginalTown







### checkorb







### checkTown







### checkOpen







### checkOrb







### test_checkkillable







### test_checkstats







### test_move







### test_capital_input







### test_invalid_input







### test_out_of_bounds






