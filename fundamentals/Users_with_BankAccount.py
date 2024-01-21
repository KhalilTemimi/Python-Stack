class BankAccount:
    bank_name = "Dojo Bank"
    all_account = []
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_account.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    def display_account_info(self):
        print(f"Balance : ${self.balance}")
        return self
    def yield_interest(self):
        if (self.balance>0):
            self.balance += (self.balance*self.int_rate)
        return self
    @staticmethod
    def can_withdraw(balance, amount):
        if (balance-amount>0):
            return True
        else:
            return False
    @classmethod
    def display_info (cls):
        for i in cls.all_account:
            print(f'Balance: {i.balance}, interest rate: {i.int_rate}')

class User:
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.account1 = BankAccount()
        self.account2 = BankAccount()
    def make_deposit(self,account,amount):
        if (account == "account1"):
            self.account1.deposit(amount)
        elif (account == "account2"):
            self.account2.deposit(amount)
        else:
            print(f"User: {self.first_name} {self.last_name} don't have this account")
        return self
    def make_withdrawal(self,account, amount):
        if (account == "account1"):
            self.account1.withdraw(amount)
        elif (account == "account2"):
            self.account2.withdraw(amount)
        else:
            print(f"User: {self.first_name} {self.last_name} don't have this account")
        return self
    def display_user_balance(self):
        print(f'User: {self.first_name} {self.last_name}, Balance account 1: {self.account1.balance}$, Balance account 2: {self.account2.balance}$')
        return self
    
will = User("Will","Smith",55)
will.make_deposit("account2",500)
will.make_deposit("account1",750)
will.display_user_balance()
will.make_withdrawal("account2",250)
will.display_user_balance()
