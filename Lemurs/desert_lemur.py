#Name: Zac Waite
#Date: April 5 2021
#Program Name: desert_lemur.py
#Purpose: Desert lemur class file for storing information about desert lemurs

import random
from lemur import Lemur
class Desert_Lemur(Lemur):
    '''Stores information about desert lemurs'''
    def __init__(self,age=None,weight=None,breed=None,gendre=None): #Constructor sets mammal age, weight and breed
        '''Take paramters age, weight, breed and gendre with None as default params'''
        super().__init__(age,weight,breed,gendre) #Calls parent constructor
        self.water_source="Cacti"
        self.coat_colour="White"
        self.baby_killer=self.water_source
    def speak(self):
        '''Print desert lemur noise'''
        print ("Desert chirp")
    def __str__(self):
        '''Outputs information about the desert lemur'''
        output=super().__str__()+"\n" #Calls parent string method
        output+="Water Source: "+self.water_source+"\n"
        output+="Coat Colour: "+self.coat_colour+"\n"
        output+="Baby Killer: "+self.baby_killer 
        return output