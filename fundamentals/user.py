class User:
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.balance = 0
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount,payee):
        self.balance -= amount
        payee.balance += amount
        return self
    def display_user_balance(self):
        print(f'User: {self.first_name} {self.last_name}, Balance: {self.balance}$')
        return self


will = User("Will","Smith", 55)
jenny = User("Jennifer", "Lopez", 53)
tom = User("Tom","Cruise",60)
will.make_deposit(200).make_deposit(100).make_deposit(300).make_withdrawal(75,tom)
jenny.make_deposit(500).make_deposit(50).make_withdrawal(200,tom).make_withdrawal(150,will)
tom.make_deposit(750).make_withdrawal(75,jenny)
will.display_user_balance()
jenny.display_user_balance()
tom.display_user_balance()