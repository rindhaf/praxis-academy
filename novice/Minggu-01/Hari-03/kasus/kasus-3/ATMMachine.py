class Deposit:
    'Class for process a deposit'
    deposit = 0
    def __init__(self):
        print("Calling constructor for Deposit class")

    def setDeposit(self, deposit):
        Deposit.deposit = deposit
    
    def getDeposit(self):
        return deposit 

class Withdraw:
    'Class for process a withdraw'
    withdraw = 0
    def __init__(self):
        print("Calling constructur for Withdraw Class")

    def setWithdraw(self, withdraw):
        Withdraw.withdraw = withdraw
    
    def getWithdraw(self):
        return withdraw

class BalanceInquiry:
    balance = 10000
    'Class for process a balance inquiry'
    
    def __init__(self):
        print("Calling constructor for Balance class")
    
    def setBalance(self, balance):
        BalanceInquiry.balance = balance
    
    def getBalance(self):
        return balance


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
        choice = 0
        select = 0
        print("====================================================")
        print("\tWelcome to this simple ATM machine")
        print("====================================================")
        print()

        print("\tPlease select ATM Transactions")
        print("\tPress [1] Deposit")
        print("\tPress [2] Withdraw")
        print("\tPress [3] Balance Inquiry")
        print("\tPress [4] Exit")
        print()
        select = int(input("\n\tWhat would you like to do? "))
        print()
        if (select < 1 or select > 4):
            print("\n\tPlease select correct transaction.")
        else:
            if select == 1:
                deposit = int(input("\tEnter the amount of money to deposit: "))
                BalanceInquiry.setBalance = BalanceInquiry.balance + Deposit.deposit
                print("Your deposit is Rp ", BalanceInquiry.balance)
            elif select == 2:
                print("\n\tTo withdraw, make sure that you have sufficient balance in your account.")
                withdraw = int(input("\tEnter amount of money to withdraw: "))
                print("Your withdraw is Rp ", withdraw)
            elif select == 3:
                print("\n\tCheck your balance.")
                print("Your deposit now is Rp ", BalanceInquiry.balance - withdraw)
            else:
                print("\n\tTransaction exited.")                

atm1 = ATMMachine()
            
