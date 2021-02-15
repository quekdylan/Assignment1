# Entity
Authors: **Dong Han**

This is a class of entities e.g.(Player, Rat, Rat King)   
Input: Name, Health, Damage, Defence, Orb=False   
Output:  Creates a object   
  
  
Example of how to initialize a entity   
player = Entity('The Hero', 20, "2-4", 1)   
print(player.health)   
  
Example of how to update variable in class   
player.health = (player.health - 1)   
print(player.health)   
  


## Methods


### __init__


This function creates the entity object 

#### Parameters
name | description | default
--- | --- | ---
name | The name of the entity (string) | 
health | The health of the entity (int) | 
damage | The damage of the entity (string) | 
defence | The defence of the entity (int) | 
orb | True if the entity is holding the Orb (bool) | False
self | - | 




