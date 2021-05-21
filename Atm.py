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
            main()

    def BalanceEnquiry(self):
        print('Balance Money left:- '+str(self.amount))
        main()

def main():
    Pinnum = int(input('Enter pin:- '))
    Cashleft = 50000
    if(Pinnum==1234):
        NextStep = input('Press X to check balance.\n\nPress Y to withdraw money\nYour Choice:- ')
        if(NextStep=='X'):
            UserDetails = Atm(Pinnum,Cashleft,0)
            UserDetails.BalanceEnquiry()
        elif(NextStep=='Y'):
            MoneyNeeded = int(input('Enter amount required:- '))
            UserDetails = Atm(Pinnum,Cashleft,MoneyNeeded)
            UserDetails.WithdrawCash()
        elif(NextStep!='X' or NextStep!='Y'):
            print('Wrong choice!')
            main()
    else:
        print('Incorrect Pin!')
        main()

main() 