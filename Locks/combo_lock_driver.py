#Name: Zac Waite
#Date: April 3 2021
#Program Name: combo_lock_driver.py
#Purpose: Create locks using the combo_lock class file, then simulate a unlocking and locking the lock
from combo_lock import Lock

def err_input(msg, limits, error="Error, please try again"): #Takes user input and throws/handles errors 
    while(True):
        try:
            value=int(input(msg))#Stores input
            if (value < limits[0] or value > limits[1]):#only takes input within limit
                error="Integer out of range. Try again."
                raise ValueError
            return value
        except ValueError:
           print(error)
print("A lock will be created with the combination you enter") 
user_lock=Lock(
    err_input("Enter the first number of the combination (1-3):", [1,3]),  #Create Lock with user input
    err_input("Enter the second number of the combination (1-3):", [1,3]), #Restrict to 1-3, as assignment instructs
    err_input("Enter the third number of the combination (1-3):", [1,3])
    )
print("\nThe lock has been created and locked with passcode", user_lock.get_combo()) #Show user combo of new lock
print("To unlock the lock, enter the correct combination")
user_lock.unlock([
    err_input("Enter the 1st digit (1-3):", [1,3]), #Prompt user to enter guesses for the lock
    err_input("Enter the 2nd digit (1-3):", [1,3]), #Put guesses into array, and use unlock function
    err_input("Enter the 3rd digit (1-3):", [1,3])  #To unlock if the array is correct.
    ])
if (user_lock.locked): print("Incorrect, still locked") #Inform user of lock state
else: print("Correct, unlocked")
random_lock=Lock() #create random lock
print("\nA new random lock has been created")
print("Try to guess the combination: ")
for i in range(3):
    random_lock.unlock([
        err_input("Guess the 1st digit (1-3):", [1,3]), #Prompt user to enter guesses for the lock
        err_input("Guess the 2nd digit (1-3):", [1,3]), #Like before, use unlock function to check array
        err_input("Guess the 3rd digit (1-3):", [1,3])
        ])
    if i==3:break #Don't output try again on last try
    if(random_lock.locked):print("Incorrect, try again \n") #If still locked, say so
    else: break #Otherwise, end loop
if(random_lock.locked):print("You were not able to unlock it, sorry. Correct combination:", random_lock.get_combo()) #If still locked, say so, and show combo
else:print(random_lock.get_combo(),"is correct! It is unlocked") #If unlocked, say so and tell them the combo was correct

    