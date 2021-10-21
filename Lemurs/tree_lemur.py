#Name: Zac Waite
#Date: April 5 2021
#Program Name: tree_lemur.py
#Purpose: Tree lemur class file for storing information about tree lemurs

import random
from lemur import Lemur
class Tree_Lemur(Lemur):
    '''Stores information about tree lemurs'''
    def __init__(self,age=None,weight=None,breed=None,gendre=None): #Constructor sets mammal age, weight and breed
        '''Take paramters age, weight, breed and gendre with None as default params'''
        super().__init__(age,weight,breed,gendre)#Calls parent constructor
        self.travels="In groups"
        self.diet="Fruit"
        self.mane="Red"
    def speak(self):
        '''Print tree lemur noise'''
        print ("Tree chirp")
    def __str__(self):
        '''Outputs information about the tree lemur'''
        output=super().__str__()+"\n" #Calls parent string method
        output+="Travels: "+self.travels+"\n"
        output+="Diet: "+self.diet+"\n"
        output+="Mane: "+self.mane 
        return output