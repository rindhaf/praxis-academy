class Deposit():
    deposit=100
    def __init__(self):
        print("Calling constructor for Deposit class")

    def setDeposit(self, depo):
        Deposit.deposit = depo
    
    def getDeposit(self):
        print("Amount deposit", Deposit.deposit)

class Withdraw:
    withdraw = 0
    def __init__(self):
        print("Calling constructur for Withdraw Class")

    def setWithdraw(self, withdraw):
        Withdraw.withdraw = wd
    
    def getWithdraw(self):
        print("Amount withdraw", Withdraw.withdraw)

class BalanceInquiry:
    balance = 0
    def __init__(self):
        print("Calling constructor for Balance class")
    
    def setBalance(self, balance):
        BalanceInquiry.balance = blnc 
    
    def getBalance(self):
        print("Amount balance", BalanceInquiry.balance)


class ATMMachine(Deposit, Withdraw, BalanceInquiry):
    
    def checkBalance(self):
        print("\tYour current balance is ", BalanceInquiry.getBalance())
    
    def withdrawMoney(self):
        if BalanceInquiry.balance == 0 :
            print("\tYour current balance is zero.")
            print("\tYou cannot withdraw!")
            print("\tYou need to deposit money first.")
        elif BalanceInquiry.balance <= 500:
            print("\tYou do not have sufficient money to withdraw")
            print("\tChecked your balance to see your money in the bank.")
        elif Withdraw.withdraw > BalanceInquiry.balance:
            print("\tThe amount you withdraw is greater than to your balance")
            print("\tPlease check the amount you entered.")
        else:
            BalanceInquiry.balance = BalanceInquiry.balance - Withdraw.withdraw
            print("\n\tYou withdraw the amount of Php ")

    def depositMoney(self):
        print("\tYou deposited the amount of ", Deposit.getDeposit())
    
    def __init__(self):
        input1 = input("Please enter your choice: ")
        select = 0
        choice = 0

        print("====================================================")
        print("\tWelcome to this simple ATM machine")
        print("====================================================")
    
        if input1 < 4 :
            print("\tPlease select ATM Transactions")
            print("\tPress [1] Deposit")
            print("\tPress [2] Withdraw")
            print("\tPress [3] Balance Inquiry")
            print("\tPress [4] Exit")

            print("\n\tWhat would you like to do? ")

        ATMMachine()