class Category:

    def __init__(self, name):
        self.name = name # It will allow the budget.Category("Food").
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description}) # Add the deposit to the list.

    def get_balance(self, amount=0):
        balance = 0
        for diposit in self.ledger: # Get every diposit on ledger list.
            balance += diposit["amount"]
        return balance

    def checkFunds(self, amount):
        return amount <= self.get_balance(amount) # Check if the amount is less than the balance got.

    def withdraw(self, amount, description=""):
        if self.checkFunds(amount): # If checkFunds function returns true, it will store the withdraw.
            self.ledger.append({"amount": -amount, "description": description}) 
            return True
        else:
            return False

    def transfer(self, amount, category):
        if (self.checkFunds(amount)):
            self.withdraw(amount, f"Transfer to {Category}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def __str__(self):
        title = f"{self.name.center(30, '*')}\n" # Specify the string to center, the width, and the characters that will fill out the string.
        itemList = ""
        total = 0
        amount = 0
        for item in self.ledger:
            amount = f"{item['amount']:>7.2f}"
            itemList += f"{item['description'][0:23]}" + f"{amount}\n"
            total += item['amount']
        str = title + itemList + f"Total: {total}"
        return str

def create_spend_chart(categories):
    cateogryNames = []
    withdraws = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total -= item['amount']
        withdraws.append(round(total, 2))
        cateogryNames.append(category.name)
    
    percentages = []
    for amount in withdraws:
        percentages.append(round(amount/sum(withdraws) * 100))
    
    graphBar = "Percentage spent by category\n"
    for i in range(100, 0, -10):
        graphBar += str(i).rjust(3) + "| "
        for perc in percentages:
            if perc >= i:
                graphBar += "o  "
            else:
                graphBar += "   "
        graphBar += "\n"

    graphBar += "   " + "-" * (len(categories) * 3 + 1) + "\n"

    longestNameLen = max([len(name) for name in cateogryNames])
    for i in range(longestNameLen):
        graphBar += "     "
        for name in cateogryNames:
            if i < len(name):
                graphBar += name[i] + "  "
            else:
                graphBar += "   "
        if i != longestNameLen - 1:
            graphBar += "\n"
    
    return graphBar

    
