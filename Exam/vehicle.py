class Vehicle (object):
    '''Add your description '''

    def __init__(self, gas_kilometrage=0, fuel_tank_size=0, fuel_available=0, km_travelled=0, num_passengers=1, fare=0, gas_price=0): 
        '''Add your description '''
        self.gas_kilometrage = gas_kilometrage
        self.fuel_tank_size = fuel_tank_size
        self.fuel_available = fuel_available
        self.km_travelled = km_travelled
        self.num_passengers=num_passengers
        self.fare=fare
        self.gas_price=gas_price

    def display_revenue(self, printer=True):
        '''Displays or returns revenue from vehicle'''
        revenue=self.num_passengers*self.fare #Revenue is fare by number of fares
        if printer: print("Revenue =",revenue) #Print if requested
        else: return revenue #Otherwise return
    
    def calculate_costs(self):
        '''returns costs from vehicle operation'''
        costs=self.km_travelled*self.gas_kilometrage/100*self.gas_price #Costs are the km by the price per km
        return costs

    def calculate_profits(self):
        '''Returns profits from passenger fares and vehicle costs'''
        profits=self.display_revenue(False)-self.calculate_costs() #Profit=revenue-cost
        return profits

    def add_fuel(self, gas):
        '''Add your description '''
        if self.fuel_tank_size - self.fuel_available >= gas:
            self.fuel_available += gas
            print("Added " + str(gas) + "L of gas to the tank.")
        else:
            print("You tried to add " + str(gas) + "L of gas.")
            print("There is only room for " + str(self.fuel_tank_size - self.fuel_available) + "L.")
    
    def drive_vehicle(self, kms):
        '''Drive the vehicle
        ex.  If the vehicle uses 9.5L/100 km then
        litres_needed = kms * 9.5 / 100 '''
        print("Drive " + str(kms) + "kms.  Start with " + str(self.fuel_available) + "L of gas.")
        litres_needed = kms * self.gas_kilometrage / 100.0
        if self.fuel_available >= litres_needed:
            self.fuel_available -= litres_needed
            self.km_travelled += kms
            print("Used " + str(litres_needed) + "L of gas.")   
        else:
            print("Ran out of fuel!")
            # Calculate how many kms were driven
            kms_this_drive= self.fuel_available*100.0 / self.gas_kilometrage
            self.km_travelled += kms_this_drive
            self.fuel_available = 0
            print("The vehicle drove " + str(kms_this_drive) + " before running out of gas.")
    
    def __str__(self):
        '''Add your description '''
        output = "Gas Kilometrage = " + str(self.gas_kilometrage) + "\n"
        output += "Fuel Tank Size = " + str(self.fuel_tank_size) + "\n"
        output += "Fuel Available = " + str(self.fuel_available) + "\n"
        output += "Kilometres Driven = "+ str(self.km_travelled) + "\n"
        output += "Passengers = "+ str(self.num_passengers) + "\n"
        output += "Fare = "+ str(self.fare) + "\n"
        output += "Fule Cost = "+ str(self.gas_price) + "\n"
        return output