#This script contains the classes in RatVenture

class Entity:
    """
    @author Dong Han
    
    This is a class of entities e.g.(Player, Rat, Rat King) \n
    Input: Name, Health, Damage, Defence, Orb=False \n
    Output:  Creates a object \n \n
    
    Example of how to initialize a entity    \n
    player = Entity('The Hero', 20, "2-4", 1) \n
    print(player.health) \n \n

    Example of how to update variable in class \n
    player.health = (player.health - 1) \n 
    print(player.health) \h
    """
    def __init__(self, name, health, damage, defence):
        """
        This function creates the entity object
        @param name The name of the entity
        @param health The health of the entity
        @param damage The damage of the entity
        @param defence The defence of the entity
        @param orb True if the entity is holding the Orb
        @param self -
        """
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence


