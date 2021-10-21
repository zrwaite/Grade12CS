#Name: Zac Waite
#Date: April 5 2021
#Program Name: my_bank_machine.py
#Purpose: Interact with ATM class to deposit, withdraw and display money in bank account
from atm import ATM

def err_input(msg, limits=[None,None], error="Error, please try again"): #Takes user input and throws/handles errors 
    while(True):
        try:
            value=float(input(msg))#Stores input
            err1=value<limits[0] if limits[0]!=None else False #Checks if smaller than min
            err2=value>limits[1] if limits[1]!=None else False #Checks if larger than max
            if (err1 or err2):#only takes input within limit
                raise ValueError
            return value
        except ValueError:
           print(error)
atm1=ATM(input("What is the name of the bank? :"), err_input("What is the initial account balance?: $", [0,None])) #Create new atm object with user input for bank name and initial account balance
while (True):
    print("*******************************")
    print("* 1:Deposit  * 2:Show Balance *") #Print options to user with numbered intructions
    print("* 3:Withdraw * 4:Add Interest *")
    print("* 5:Quit                      *")
    print("*******************************")
    option=err_input("What would you like to do?: ", [1,5]) #Take user input of options within specific range.
    if(option==1): atm1.deposit(err_input("How much would you like to deposit? :$", [0, None])) #If specified, call atm deposit function
    if(option==2): print(atm1.display()) #If specified, display atm's account balance
    if(option==3): atm1.withdraw(err_input("How much would you like to withdraw? :$", [0, None])) #If specified, call atm withdraw fucntion
    if(option==4): print(atm1.add_interest(err_input("What is the annual interest rate? (%):", [0, None]), err_input("What is the number of days? :", [0, None]))) #If specified, call atm interest calculator function and use user input
    if(option==5): break #If specified, quit program.