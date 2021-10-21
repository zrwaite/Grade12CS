#Name: Zac Waite
#Date: April 5 2021
#Program Name: lemur.py
#Purpose: Lemur class file for storing information about Lemurs

import random
from mammal import Mammal
class Lemur(Mammal):
    '''Stores information about lemurs'''
    def __init__(self,age=None,weight=None,breed=None,gendre=None): #Constructor sets mammal age, weight and breed
        '''Take paramters age, weight, breed and gendre with None as default params'''
        super().__init__(age,weight,breed,gendre) #Calls parent constructor
        if (self.age==None):self.age=random.randint(0, 19) #If lemur has no age, give random age
        if (self.weight==None):self.weight=random.randint(10, 50)/10.0 #If lemur has no age, give random age
        if (self.gendre==None): self.gendre="Female" if random.randint(0,1) else "Male" #If lemur has no gendre, give random gendre
        self.breed="Lemur"
        self.location="Madagascar"
        self.coat="fur"
        self.classification="Prosimain"
        self.comb="Teeth"
        self.dominant_g="Female"
        self.dominant=True if self.gendre==self.dominant_g else False #Dominant if female
    def speak(self):
        '''Print mammal noise'''
        print ("Chirp")
    def __str__(self):
        '''Outputs information about the lemurs'''
        output=super().__str__()+"\n" #Calls parent string method
        output+="Location: "+self.location+"\n"
        output+="Classification: "+self.classification+"\n"
        output+="Comb: "+self.comb+"\n"
        output+="Dominant?: "+str(self.dominant)
        return output