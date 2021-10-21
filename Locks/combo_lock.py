#Name: Zac Waite
#Date: April 2 2021
#Program Name: combo_lock.py
#Purpose: Lock class file for storing different combinations and information about locks

import random

class Lock(object):
    '''Stores information about locks'''
    def __init__(self, num1=0, num2=0, num3=0):
        '''Take paramters for three digit code with 0 as default params'''
        nums=[num1, num2, num3] #List of numbers from input
        self.combo=[] #Combiantion starts as empty list
        self.locked=True #Starts locked
        for num in nums: self.combo.append(num if num else random.randint(1,3)) #Fills in combo list with either input or random numbers
    def get_combo(self):
        '''Getter for combination'''
        return str(self.combo)[1:len(str(self.combo))-1] #To get passcode
    def set_combo(self, array=[]): #To set passcode 
        '''Setter for combination'''
        if (self.locked):return #(only allowed if unlocked)
        try: 
            for i in range(len(array)):self.combo[i]=int(array[i]) #Does not input incorrect values or empty values
        except (ValueError, IndexError): return
    def unlock(self, combo): 
        '''Checks combination and unlocks lock'''
        if (combo==self.combo): self.locked=False #If inputted combination matches combination, unlock
    def lock(self):
        '''Locks lock'''
        self.locked=True #Sets locked to true, locks lock