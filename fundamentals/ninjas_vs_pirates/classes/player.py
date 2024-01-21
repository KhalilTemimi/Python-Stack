class Player():
    def __init__(self,name):
        self.name = name
    
    @staticmethod
    def can_attack(health):
        if (health>=0):
            return True
        else:
            return False