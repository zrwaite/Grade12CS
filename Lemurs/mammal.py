#Name: Zac Waite
#Date: April 5 2021
#Program Name: mammal.py
#Purpose: Mammal class file for storing information about mammals

import random
class Mammal(object):
    '''Stores information about mammals'''
    def __init__(self,age=None,weight=None,breed=None,gendre=None): #Constructor sets mammal age, weight and breed
        '''Take paramters age, weight, breed and gendre with None as default params'''
        self.age=age #Int age of animal
        self.weight=weight#Int weight of animal
        self.breed=breed #String breed of animal
        self.gendre=gendre #String gendre of animal
    def get_age(self):
        '''Getter for age'''
        return self.age #Accesses object's age
    def get_weight(self): 
        '''Getter for weight'''
        return self.weight #Accesses object's weight
    def get_breed(self): 
        '''Getter for breed'''
        return self.breed #Accesses object's breed
    def get_gendre(self): 
        '''Getter for gendre'''
        return self.gendre #Accesses object's gendre
    def set_age(self,new_age): 
        '''Setter for age'''
        self.age=new_age #Changes object's age
    def speak(self):
        '''Print mammal noise'''
        print ("Default: The mammal speaks.")
    def __str__(self):
        '''Outputs information about the mammal'''
        output="Age: "+str(self.age)+"\n"
        output="Weight: "+str(self.weight)+"\n"
        output="Breed: "+self.breed+"\n"
        output="Gendre: "+self.gendre
        return output
