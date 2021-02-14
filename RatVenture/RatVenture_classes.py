#This script contains the classes in RatVenture

class Entity:
    """
    This is a class of entities e.g.(Player, Rat) \n
    Input: Name, Health, Damage, Defence \n
    Output:  Creates a object
    @author Dong Han
    """

    def __init__(self, name, health, damage, defence):
        """
        description: This function creates the entity object
        @param name The name of the entity, test
        @param health The health of the entity
        """
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence



# Example of how to initialize a entity    
# player = Entity('The Hero', 20, "2-4", 1)
# print(player.health)

# Example of how to update variable in class
# player.health = (player.health - 1)
# print(player.health)

