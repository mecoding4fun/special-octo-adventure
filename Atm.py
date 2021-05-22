class Atm:
    def __init__(self, pin, amount, cashNeeded):
        self.pin = pin
        self.amount = amount
        self.cashNeeded = cashNeeded

    def WithdrawCash(self):
        if(self.cashNeeded>self.amount):
            print('Insufficient balance')
        else:
            self.amount = self.amount-self.cashNeeded
            print('\nWithdrawed amount:- '+str(self.cashNeeded)+'\n'+'Balance Money left:- '+str(self.amount))
            Check=input('Startover again?\n1 - Yes\n2 - No\n:- ')
            if(Check==1):
                main()

    def BalanceEnquiry(self):
        print('Balance Money left:- '+str(self.amount))
        Check=input('Startover again?\n1 - Yes\n2 - No\n:- ')
        if(Check==1):
            main()

    def DepositCash(self):
        DepositAmount = int(input('Enter money to be deposited:- '))
        self.amount = self.amount+DepositAmount
        print('\nDeposited cash:- '+str(DepositAmount)+'\n'+'Money left:- '+str(self.amount))
        Check=input('Startover again?\n1 - Yes\n2 - No\n:- ')
        if(Check==1):
            main()

def main():
    Pinnum = int(input('Enter pin:- '))
    Cashleft = 50000
    if(Pinnum==1234):
        proj(Pinnum,Cashleft)
    else:
        print('Incorrect Pin!')
        main()

def proj(PinNum,CashLeft):
    NextStep = input('Press X to check balance.\n\nPress Y to withdraw money\n\nPress Z to Deposit cash\nYour Choice:- ')
    if(NextStep=='X'):
        UserDetails = Atm(PinNum,CashLeft,0)
        UserDetails.BalanceEnquiry()
    elif(NextStep=='Y'):
        MoneyNeeded = int(input('Enter amount required:- '))
        UserDetails = Atm(PinNum,CashLeft,MoneyNeeded)
        UserDetails.WithdrawCash()
    elif(NextStep=='Z'):
        UserDetails = Atm(PinNum,CashLeft,0)
        UserDetails.DepositCash()    
    elif(NextStep!='X' or NextStep!='Y' or NextStep!='Z'):
        print('Wrong choice!')
        proj(PinNum,CashLeft)

main() 
