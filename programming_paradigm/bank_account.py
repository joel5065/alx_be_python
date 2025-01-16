class BankAccount:
   
    def __init__(self, account_balance = 0.00):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
    
    def withdraw(self, amount):
        if self.account_balance < amount:
            return False
        self.account_balance -= amount
        return True
    
    def display_balance(self):
        print(f"Current Balance: ${"%.2f" % self.account_balance}")
    