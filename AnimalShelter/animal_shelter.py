#Name: Zac Waite
#Date: April 8 2021
#Program Name: animal_shelter.py
#Purpose: Animal shelter class file for storing information about animal shelters containing dogs

import random
from dog import Dog
class AnimalShelter(object):
    '''Stores information about animal shleters'''
    def __init__(self,num_dogs=0): #Constructor sets mammal age, weight and breed
        '''Take paramters age, weight, breed and gendre with None as default params'''
        self.num_dogs=int(num_dogs) #Number of dogs in the shelter
        self.dogs=[] #Stores all dog objects
        for i in range(self.num_dogs):self.dogs.append(Dog("", "")) #Adds dogs for number of dogs inputted
    def get_num_dogs(self):
        '''Getter for number of dogs'''
        return self.num_dogs
    def get_dog(self, num):
        '''Getter for specific dog at index num'''
        try:
            output=self.dogs[num]
            return output
        except IndexError:
            return None
    def add_dog(self, name, breed, age=-1):
        '''Adds dog to list of dogs'''
        age=int(age) #Parses age
        self.dogs.append(Dog(name, breed, age)) #Adds dog with inputted info
        self.num_dogs+=1 #Incremenent num dogs
    def remove_dog(self, num=-1):
        '''Removes dog from list of dogs'''
        if (num<0):num=random.randint(0, len(self.dogs)-1) #If no inded is inputted , generate random input
        del self.dogs[num] #Delete specified dog
        self.num_dogs-=1 #Decrement dog
    def calculate_costs(self): #Calculates maintenence costs of shelter
        daily_cost=self.num_dogs*15 #Daily is $15 per dog
        monthly_cost=round(daily_cost*30.436875*100)/100.0 #Monthly average is daily cost times average days per month
        yearly_cost=round(daily_cost*365.2422*100)/100.0 #Yearly average is daily cost times average days in a year
        output="$"+str(daily_cost)+" per day\n"
        output+="$"+str(monthly_cost)+" per month on average\n"
        output+="$"+str(yearly_cost)+" per year on average\n"
        return output
    def __str__(self):
        '''Outputs information about the lemurs'''
        output=""
        for i in range(self.num_dogs): #Outputs every dog
            output+="Dog#"+str(i+1)+": "+str(self.dogs[i])+"\n"
        return output