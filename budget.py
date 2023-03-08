class Category:

    def __init__(self, name):
        self.name = name # It will allow the budget.Category("Food").
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description}) # Add the deposit to the list.

    def withdraw(self, amount, description=""):
        if checkFunds(amount): # If checkFunds function returns true, it will store the withdraw.
            self.ledger.append({"amount": -amount, "description": description}) 
            return True
        else:
            return False

    def get_balance(self, amount):
        balance = 0
        for diposit in self.ledger: # Get every diposit on ledger list.
            balance += diposit["amount"]
        return balance

    def checkFunds(self, amount):
        return amount <= self.get_balance(amount) # Check if the amount is less than the balance got.

    def transfer(self, amount, Category):
        # Add code.

    #def create_spend_chart(categories):
    
