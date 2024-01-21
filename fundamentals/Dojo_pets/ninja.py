import pets

class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self,first_name,last_name,treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = None
        self.pet_food = pet_food
        self.pet = pets.Pets(" "," "," ")

# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        print(f"{self.first_name} feed his pet {self.pet.name}")
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self



max = pets.Pets("Max","Dog","catch things")
tom = pets.Pets("Tom","Cat","rubbing")
momochi = Ninja("Momochi","Sandayu",None,"meat")
momochi.pet = max
momochi.feed()
momochi.bathe()