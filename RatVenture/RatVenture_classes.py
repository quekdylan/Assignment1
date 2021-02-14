#This script contains the classes in RatVenture

class Entity:
    '''
    This is a class of entities e.g.(Player, Rat)
    Input: Name, Health, Damage, Defence
    Output:  Creates a object
    '''

    def __init__(self, name, health, damage, defence):
        '''
        self.name = Name of entity
        self.health = Health of entity
        self.damage = Damage of entity
        self.defence = Defence of entity
        '''
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

