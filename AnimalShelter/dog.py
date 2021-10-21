#Name: Zac Waite
#Date: April 2 2021
#Program Name: dog.py
#Purpose: Dog class file for storing different names and information about dogs

import random

class Dog(object):
    '''Stores information about dogs'''
    def __init__(self, name, breed, age=-1, agression=-1, hunger=-1):
        '''Takes parameters name, breed, age, agression, and hunger, with randomly generated values if not inputted'''
        if(hunger==-1):self.hunger=random.randint(1, 10) #Randomly generates hunger if not set
        else: self.hunger=hunger
        if(agression==-1):self.agression=random.randint(1,10) #Randomly generates aggresion if not set
        else: self.aggression=agression
        if(age==-1):self.age=random.randint(1, 10) #Randomly generates age if not set
        else: self.age=age
        if(not breed):
            breeds=["Poddle", "Bulldog", "Retreiver", "Husky", "Chihuahua", "Pomeranian"]
            self.breed=breeds[random.randint(0,len(breeds)-1)] #Randomly generates breed from list if not set
        else: self.breed=breed
        if(not name):
            names=["Peta", "Andy", "Jamie", "Johnny", "Phil", "Nate", "Matt", "Tom", "Dude"]
            self.name=names[random.randint(0, len(names)-1)] #Randomly generaets name from list if not set
        else: self.name=name  
        self.mood=-10-self.agression-self.hunger #Mood is given an initial value from calculation
    def __str__(self):
        '''Outputs all information about the dog. '''
        output= self.name+", a "+self.breed+" is "+str(self.age)+" years old. Agression: "+str(self.agression)+"; Hunger: "+str(self.hunger)
        return output #Outputs all informaiton about the dog
    def get_name(self):
        '''Getter for name'''
        return self.name #To get name
    def get_breed(self):
        '''Getter for breed'''
        return self.breed #To get breed
    def get_age(self):
        '''Getter for age'''
        return self.age #To get age
    def get_agression(self):
        '''Getter for agression'''
        return self.agression #To get agression
    def get_hunger(self):
        '''Getter for hunger'''
        return self.hunger #To get hunger
    def set_name(self, new_name):
        '''Setter for name'''
        self.name=new_name #To set name
    def set_breed(self, new_breed):
        '''Setter for breed'''
        self.breed=new_breed #To set breed
    def set_age(self, new_age):
        '''Setter for age'''
        self.age=new_age #To set age
    def set_agression(self, new_agression):
        '''Setter for agression'''
        self.agression=new_agression #To set agression
    def set_hunger(self, new_hunger): 
        '''Setter for hunger'''
        self.hunger=new_hunger #To set hunger
    def get_mood(self): #To get and set mood 
        '''Getter for mood'''
        self.mood=10-self.agression-self.hunger
        return self.mood
    def bark(self): #To bark based on mood
        '''Outputs bark based on mood'''
        if(self.get_mood()>0):return "Woof woof"
        else: return "Grrr...ARF ARF!"