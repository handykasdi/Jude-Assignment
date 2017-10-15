from account import account
class costumer(account):
    def __init__(self,balance,firstName,lastName,account):
        super().__init__(self,balance)
        self.firstName=firstName
        self.lastName=lastName
        self.account=account
    def Costumer(self):
        f=str()
        l=str()
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName

    def get_account(self):
        return self.account

    def set_account(self,value):
        self.account= value
