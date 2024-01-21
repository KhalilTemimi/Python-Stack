from classes.player import Player

class Ninja(Player):

    def __init__( self , name ):
        super().__init__(name)
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength} Speed: {self.speed} Health: {self.health}\n")
        return self

    def attack( self , pirate ):
        if Player.can_attack(self.health):
            pirate.health -= self.strength
            self.strength += 5
            print(f"\n{self.name} attacked {pirate.name}\n")
        else:
            print(f"Hey {self.name} you are too week you cannot attack!!!")
        return self