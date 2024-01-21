class Pets:
# implement __init__( name , type , tricks )
    def __init__(self,name,type,tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5 
        self.health += 10
        return self
# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        return self
# noise() - prints out the pet's sound
    def noise(self):
        Dog.noise(self)
        return self

class Dog(Pets):
    def __init__(self, name, type, tricks):
        super().__init__(name, tricks)
        self.type = type
    def noise(self):
        print(f"{self.name} is a {self.type} he barks")
        return self
