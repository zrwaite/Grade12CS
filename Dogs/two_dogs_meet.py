#Name: Zac Waite
#Date: April 2 2021
#Program Name: two_dogs_meet.py
#Purpose: Create dogs using the dog class file, then simulate a meeting between them.
import dog

def err_input(msg, limits, error="Error, please try again"): #Takes user input and throws/handles errors 
    while(True):
        try:
            value=int(input(msg))#Stores input
            if (value < limits[0] or value > limits[1]):#only takes input within limit
                return False
            return value
        except:
           return False

print("Two dogs will be created in this simulation")
dog1=dog.Dog(input("Please enter a name for the first dog: "), input("Please enter the breed of the first dog: ")) #Create 2 dogs with user input
dog2=dog.Dog(input("Please enter a name for the second dog: "), input("Please enter the breed of the second dog: "))
dogs=[dog1, dog2] #Create array of dogs for less code
for i in range(len(dogs)):
    print("\n"+str(dogs[i])) #For each dog, print dog info
    print("To set a new agression, enter a number from 1-10")
    new_agr=err_input("Enter anything else to skip: ", [1, 10]) #prompt user for new agression, and 
    if (new_agr):dogs[i].set_agression(new_agr)                 #set it if needed
    print(dogs[i])
    print("To set a new hunger, enter a number from 1-10")
    new_hun=err_input("Enter anything else to skip: ", [1, 10]) #prompt user for new hunger, and
    if (new_hun):dogs[i].set_hunger(new_hun)                    #set it if needed
print("\nMeeting:")
for i in range(len(dogs)): #For each dog, print the name and the appropriate bark
    print(dogs[i].get_name()+": "+dogs[i].bark())
