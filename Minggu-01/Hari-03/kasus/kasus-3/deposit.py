class Deposit():
    deposit=100
    def __init__(self):
        print("Calling constructor for Deposit class")

    def setDeposit(self, depo):
        Deposit.deposit = depo
    
    def getDeposit(self):
        print("Amount deposit", Deposit.deposit)