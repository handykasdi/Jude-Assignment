from costumer import account
class bank(account):
    def __init__(self,costumer,numberOfCostumer,bankName):
        account.__init__(self,costumer)
        self.numberOfCostumer=numberOfCostumer
        self.bankName=bankName
    def bank(self):
        return self.bankName
    def addCostumer(self):
        cos=[]
        f=input("first name:")
        l=input("last name: ")
        FnL= f + l
    def get_numberOfCostumer(self):
        return self.numberOfCostumer
    def get_costumer(self,costumer):
        self.costumer = costumer
