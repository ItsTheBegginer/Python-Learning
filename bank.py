#OOP
class Bank:
    def __init__(self, owner , balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        else:                   
            print(f"Depositing {amount}$ in {self.owner}'s account...")
            self.balance += amount
            print(f"Balance = {self.balance}$")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
            return
        elif amount <= 0:
            print("Withdraw amount must be positive")
            return                      
        else:
            print(f"Withdrawing {amount}$ from {self.owner}'s account...")
            self.balance -= amount
            print(f"Balance = {self.balance}$")




John_Account = Bank("John",1000)
John_Account.deposit(500)           
John_Account.withdraw(2000)
John_Account.withdraw(300)
John_Account.deposit(-100)