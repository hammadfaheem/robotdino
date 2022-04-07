from weapon import Weapon 

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("ak47" , 50)


    def attack(self, dinosaur):
        #lower dino's health by robots weapon
        dinosaur.health -= self.active_weapon.attack_power
        