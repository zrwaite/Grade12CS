import vehicle

def err_input(msg, limits=[None,None], error="Error, please try again"): 
    '''Takes user input and throws/handles errors'''
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
num_passengers=int(err_input("How many passengers?: ", [1,None]))
fare=err_input("Passenger fare?: ", [0,None])
gas_price=err_input("What is the price of gas today in $/L ?: ", [0,None])
print()
car1 = vehicle.Vehicle(7.5, 60.0, 60.0, 0.0, num_passengers, fare, gas_price)
#Show Vehicle Info
print(car1)
car1.display_revenue() #Show revenue from passengers

#Drive car for 100km
car1.drive_vehicle(100.0)
print(car1)

#Drive car for 450 kms
car1.drive_vehicle(450.0)
print(car1)

#Try to drive 1000 km - runs out of gas
car1.drive_vehicle(1000.0)
print(car1)

#Add 25L of gas
car1.add_fuel(25.0)
print(car1)

#Try to add 100 L of gas
car1.add_fuel(100.0)
print(car1)

print()
car1.display_revenue() #Display revenue from passengers
print("Cost =",car1.calculate_costs()) #Display costs in total for the trip
print("Profit =",car1.calculate_profits()) #Display profits in total for the trip
