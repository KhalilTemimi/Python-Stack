class animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.health = 100
        self.happiness = 100
    def display_info(self):
        print(f"Animal's Name: {self.name}, Health Level: {self.health}, Happiness Level: {self.happiness}")
        return self
    def feed (self):
        self.health += 10
        self.happiness += 10
        return self
class lions(animal):
    def __init__(self,name,age,food):
        super().__init__(name,age)
        self.health = 180
        self.happiness = 150
        self.food = food
class tigers(animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 150
        self.happiness = 150
class bears(animal):
    def __init__(self, name, age, french_name):
        super().__init__(name, age)
        self.health = 120
        self.happiness = 120
        self.french_name = french_name

