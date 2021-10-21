#Name: Zac Waite
#Date: April 5 2021
#Program Name: my_bank_machine.py
#Purpose: Use lemur classes to generate random lemurs

from  jungle_lemur import Jungle_Lemur
from tree_lemur import Tree_Lemur
from desert_lemur import Desert_Lemur

def err_input(msg, limits=[None,None], error="Error, please try again"): #Takes user input and throws/handles errors 
    while(True):
        try:
            value=float(input(msg))#Stores input
            err1=value<limits[0] if limits[0]!=None else False #Checks if smaller than min
            err2=value>limits[1] if limits[1]!=None else False #Checks if larger than max
            if (err1 or err2):#only takes input within limit
                raise ValueError
            return value
        except ValueError:
           print(error)
lemur_types=[] #Stores names of types of lemurs
lemurs=[] #Stores different lemur objects
for i in range(2):
    user_choice=err_input("Select the species of lemur "+str(i+1)+" (1-3): ", [1,3]) #User selects species of lemur within input
    if(user_choice==1): #If choice is one, generate tree lemur
        lemur_types.append("Tree Lemur")
        lemurs.append(Tree_Lemur())
    elif(user_choice==2): #If choice is two, generate desert lemur
        lemur_types.append("Desert Lemur")
        lemurs.append(Desert_Lemur())
    elif(user_choice==3): #If choice is three, generate jungle lemur
        lemur_types.append("Jungle Lemur")
        lemurs.append(Jungle_Lemur())
for i in range(2): 
    print("Creating", lemur_types[i]) #Tell user what lemur types are being created
for i in range(2): 
    print("\n\t"+lemur_types[i]) #Print lemur information
    print(lemurs[i])