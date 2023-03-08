class Category:

    def __init__(self, name):
        self.name = name # It will allow the budget.Category("Food").
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description}) # Add the deposit to the list.


#def create_spend_chart(categories):
    
