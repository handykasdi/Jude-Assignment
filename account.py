class account:
    def __init__(self,balance):
        self.balance= balance
    def get_balance(self):
        return self.balance

    def deposit(self,value):
        self.balance += value

    def withdraw(self,value):
        self.balance -= value
