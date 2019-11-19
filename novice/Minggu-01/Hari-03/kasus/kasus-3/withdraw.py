class Withdraw:
    withdraw = 0
    def __init__(self):
        print("Calling constructur for Withdraw Class")

    def setWithdraw(self, withdraw):
        Withdraw.withdraw = wd
    
    def getWithdraw(self):
        print("Amount withdraw", Withdraw.withdraw)