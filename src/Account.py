class Account:
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 10000
        self.holder = account_holder

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds :('  
        self.balance -= amount
        return self.balance

my_account = Account('Matt')        
sean_account = Account('Sean')

print(my_account.interest)
Account.interest = 0.04
print(my_account.interest)
