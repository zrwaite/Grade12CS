import car

def err_input(msg, error="Error, please try again"): #Takes user input and throws/handles errors 
    while(True):
        try:
            value=int(input(msg))#Stores input
            return value
        except:
            print(error)
def bool_input(msg): # Takes user input of hopefully y or n
    value=input(msg)
    if (value.lower()=="y"): return True #if y, then return True
    return False #Otherwise (hopefully n) return False

random_car=car.Car() #Generate random car
user_car=car.Car( #User generates car with inputs:
    input("What is the make of the car?: "),  #User input for make of car
    input("What is the model of the car?: "),  #User input for model of car
    err_input("What is the year of the car?: "), #User input for int year of car
    err_input("What is the price of the car?: "), #User input for int price of car
    input("What is the colour of the car?: "), #User input for colour of car
    bool_input("Is the car electric? (y/n): "))#User input for electricity of car
print("The random car is: ")
print(random_car) 
print("Your car is: ")
print(user_car)
user_car.horn() #Honk horn