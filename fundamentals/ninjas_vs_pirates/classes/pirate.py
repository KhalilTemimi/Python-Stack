from classes.player import Player

class Pirate(Player):

    def __init__( self , name ):
        super().__init__(name)
        self.strength = 15
        self.speed = 3
        self.health = 0

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength} speed: {self.speed} Health: {self.health}\n")
        return self

    def attack ( self , ninja ):
        if Player.can_attack(self.health):
            ninja.health -= self.strength
            self.strength += 5
            print(f"\n{self.name} attacked {ninja.name}\n")
        else:
            print(f"Hey {self.name} you are too week you cannot attack!!!")
        return self
    

