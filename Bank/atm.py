#Name: Zac Waite
#Date: April 5 2021
#Program Name: atm.py
#Purpose: Class file to store information about bank accounts with atm

class ATM(object):
    '''Stores information about bank accounts'''
    def __init__(self, bank, balance=0): #Constructor takes bank name and initial balances
        '''Takes parameters for bank name and balance in canadian dollars'''
        self.bank=bank #Name of bank
        self.balance=balance #Account balance 
        self.currency="CAD" #Account currency, just added as another important attribute
    def deposit(self, amount): #Adds amount to bank account balance
        '''Inputs amount of money to add to balance'''
        self.balance+=amount
        print("$"+str(amount)+" has been added to the account.")
    def withdraw(self, amount): #Takes amount from bank account balance
        '''Inputs amount of money to remove from balance'''
        if (self.balance>amount): 
            self.balance-=amount
            print("$"+str(amount)+" has been taken from the account.")
        else: #If that amount of money is too big, do not complete transaction
            print("Transaction could not be completed, account does not possess $"+str(amount))
    def display(self): #Display current balance with message.
        '''Displays current balance'''
        return "Current Balance: $" + str(self.balance)
    def add_interest(self, an_int, n): #Use interest formula to calculate new balance
        '''Calculates and adds interest to current balance'''
        i=an_int/(365*100) #interest decimal
        P=self.balance #Present value 
        Interest=round((P*(1+i)**n-P)*100)/100.0 #Interest generated
        self.balance+=Interest #Add interest to bank account
        return "Interest added: " + str(Interest) #Display added amount to user. 