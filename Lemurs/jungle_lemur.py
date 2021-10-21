#Name: Zac Waite
#Date: April 5 2021
#Program Name: tree_lemur.py
#Purpose: Tree lemur class file for storing information about tree lemurs

import random
from lemur import Lemur
class Jungle_Lemur(Lemur):
    '''Stores information about jungle lemurs'''
    def __init__(self,age=None,weight=None,breed=None,gendre=None): #Constructor sets mammal age, weight and breed
        '''Take paramters age, weight, breed and gendre with None as default params'''
        super().__init__(age,weight,breed,gendre) #Calls parent constructor
        self.travels="In small groups"
        self.diet="Mice, snails and insects"
        self.mane="None"
        self.coat_colour="Blue" if random.randint(0,1) else "Black" #Coat colour is randomly either blue or black
    def speak(self):
        '''Print jungle lemur noise'''
        print ("Jungle chirp")
    def __str__(self):
        '''Outputs information about the jungle lemur'''
        output=super().__str__()+"\n" #Calls parent string method
        output+="Travels: "+self.travels+"\n"
        output+="Diet: "+self.diet+"\n"
        output+="Mane: "+self.mane+"\n"
        output+="Coat Colour: "+self.coat_colour+"\n"
        return output