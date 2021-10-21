#Name: Zac Waite
#Date: March 30 2021
#Program Name: car.py
#Purpose: Car class file for storing different models and inforamtion about cars

import random
class Car(object):
    def __init__(self, make="", model="", year=0, price=0, colour="", electric=False):
        self.make=make #Make of the car
        self.model=model #Model of the car
        self.year=year #Year of the car
        self.price=price #Price of the car
        self.electric=electric #If the car is an electric car
        self.colour=colour #colour of the car
        honks=["Beep", "Honk", "Bleep", "Blaaap"] #Different horn sounds
        self.honk=honks[random.randint(0,len(honks)-1)] #Horn is a random one of the sounds
        if (not self.make):
            makes={ #If the make is not one of the ones specified, 
                "Tesla":["Model S", "Model 3", "Model X"], 
                "Hyundai":["Elantra", "Lafesta", "Celesta"], 
                "Acura":["TLX", "RDX", "ILX"], 
                "Ford":["Escape", "Bronco", "F-150"], 
                "Dodge":["Challenger", "Charger", "Durango"]} #Use this dictionary of arrays for make and model
            self.make=list(makes.keys())[random.randint(0,len(makes)-1)] #Make is a random one of the dictionary keys
            self.model=makes[self.make][random.randint(0,len(makes[self.make])-1)] #Make is a random array value at the dictionary key's value
            if (self.make=="Tesla"):
                self.electric=True #If the randomly generated car is a tesla, it is electric
        if (not self.price): #If no price is specified
            self.price=random.randint(100, 500)*100 #Random price from 10000-50000, in measurements of 100
        if (not self.colour):
            colours=["Black", "White", "Red", "Yellow", "Blue", "Green"] #If no colour is specified, 
            self.colour=colours[random.randint(0,len(colours)-1)] #the colour is a random one from the list
        if (not self.year):
            self.year=random.randint(2010,2021) #If no year is specified, pick a random one frmo 2010-2021
    def __str__(self): #Outputs values of the object in a readable fashion
        output=self.colour+" "+str(self.year)+" "+self.make+" "+self.model+", $"+str(self.price)+", "+"not "*int(not self.electric)+"electric"
        return output
    def horn(self):  #Honks the horn
        print(self.honk) #Honk honk