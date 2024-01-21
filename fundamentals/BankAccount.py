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
    def withdraw(self, amount, payee):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
            payee.balance += amount
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
will = BankAccount()
jenny = BankAccount()
will.deposit(200).deposit(750).deposit(100).withdraw(75,jenny).yield_interest().display_account_info()
jenny.deposit(750).deposit(300).withdraw(60,will).withdraw(65,will).withdraw(25,will).withdraw(150,will).yield_interest().display_account_info()
BankAccount.display_info()

