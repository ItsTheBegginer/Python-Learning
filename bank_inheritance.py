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
            
class SavingsAccount(Bank):
    def __init__(self, owner, balance,limit,interest):
        super().__init__(owner, balance)
        self.limit = limit
        self.interest = interest
    def withdraw(self,amount):
        if amount> self.balance:
            print("Insufficient Balance!")
        elif amount > self.limit:
            print("limit exceeded!")
            return
        elif amount <= 0:
            print("Withdraw amount must be positive")
            return                      
        else:
            print(f"Withdrawing {amount}$ from {self.owner}'s account...")
            self.balance -= amount
            print(f"Balance = {self.balance}$")

class Current(Bank):
    def __init__(self, owner, balance,limit):
        super().__init__(owner, balance)
        self.limit = limit
    
    def withdraw(self,amount):
        if self.balance - amount <-200:
            print("Insufficient Balance!")
        elif amount > self.limit:
            print("limit exceeded!")
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
print("\nSavings\n")
Adam = SavingsAccount("Adam" , 20000 , 200 , 10)
Adam.deposit(100)
Adam.withdraw(500)
Adam.withdraw(199)
Adam.withdraw(250)
print("\nCurrent\n")
Eve = Current("Eve" , 5000 , 1000)
Eve.deposit(500)        
Eve.withdraw(2000)
Eve.withdraw(4000)
Eve.withdraw(800)
Eve.deposit(-50)    
Eve.withdraw(-100)