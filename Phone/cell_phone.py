import random
class CellPhone (object):
    '''Stores information about cellphones'''
    def __init__(self, carrier="", type="", speed=-1, memory=-1, num_apps=-1):
        '''Takes parameters carrier, type, speed, memory, and num_apps, with randomly generated values if not inputted'''
        #Public
        if not(type): #Generates random phone type if no type
            types=["IPhone", "Android", "Pixel", "Huwei", "LG"]
            self.type=types[random.randint(0,len(types)-1)]
        else:self.type=type #Uses inputted type
        #Protected
        if not(carrier): #Generates random carrier if no carrier
            carriers=["Verizon", "AT&T", "Sprint", "T-Mobile", "Virgin", "Rogers"]
            self._carrier=carriers[random.randint(0,len(carriers)-1)]
        else:self._carrier=carrier #Uses inputted carrier
        #Protected
        if (num_apps==-1): self._num_apps=random.randint(0, 8) #Generates random number of apps if no apps
        else: self._num_apps=int(num_apps) #Uses inputted number of apps
        #Private
        if (speed==-1):self.__speed=float(random.randint(8, 20)/10.0) #Generates random speed if no speed
        else: self.__speed=float(speed) #Uses inputted speed
        #Private
        if (memory==-1): self.__memory=float(2**random.randint(3,7)) #Generates random memory if no memory
        else: self.__memory=float(memory) #Uses inputted memory
    def get_type(self):
        '''Getter for type'''
        return self.type
    def get_carrier(self):
        '''Getter for carrier'''
        return self._carrier
    def get_num_apps(self):
        '''Getter for num_apps'''
        return self._num_apps
    def get_speed(self):
        '''Getter for speed'''
        return self.__speed
    def get_memory(self):
        '''Getter for memory'''
        return self.__memory
    def set_type(self, new_type):
        '''Setter for type'''
        self.type=new_type
    def set_carrier(self, new_carrier):
        '''Setter for carrier'''
        self._carrier=new_carrier
    def set_num_apps(self, new_num_apps):
        '''Setter for num_apps'''
        try:
            self._num_apps=int(new_num_apps)
        except ValueError:
            pass
    def set_speed(self, new_speed):
        '''Setter for speed'''
        try:
            self.__speed=float(new_speed)
        except ValueError:
            pass
    def set_memory(self, new_memory):
        '''Setter for memory'''
        try:
            self.__memory=float(new_memory)
        except ValueError:
            pass