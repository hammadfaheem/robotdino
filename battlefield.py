from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot("mrx")
        self.dinosaur =  Dinosaur("trex" , 35)
        
    def run_game(self):

        # This while loop runs until either robot or dinosaur wins the battle.
        while True:
            player = input("Who attack ?")

            #Condition: When user want to attack on Dinosaur by Robot
            if player == "r":
                if self.dinosaur.health > 0:
                    self.robot.attack(self.dinosaur)
                    ###############################

                    if self.dinosaur.health <=0:
                        print("Robot Wins")
                        break
                    else:
                        print("Robot Health: {}".format(self.robot.health))
                        print("Dinosaur Health: {}".format(self.dinosaur.health))
                        ##################################

                else:
                    print("Robot Wins")
                    break


            # Condition: When user want to attack on Robot by Dinosaur    
            elif player == "d":
                if self.dinosaur.health >0:
                    self.dinosaur.attack(self.robot)
                    #################################

                    if self.robot.health <=0:
                        print("Dinosaur Wins")
                        break
                    else:
                        print("Robot Health: {}".format(self.robot.health))
                        print("Dinosour Health: {}".format(self.dinosaur.health)) 
                        ##############################################
                else:
                    print("Dinasaur Wins")
                    break

    # Don't need this stuff                
    #def display_welcome(self):
    #    pass
    #def battle_phase(self):
    #   pass
    #def display_winner(self):
    #    pass


