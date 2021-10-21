#Name: Zac Waite
#Date: March 13 2021
#Program Name: Resistors.py
#Purpose: Calculates resistance from colour schemes
import random
import re
colours = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"] #colours in order
def err_input(msg, error="Error, please try again"): #Takes user input and throws/handles errors 
    while(True):
        try:
            value=input(msg)#Stores input
            pattern=r"^[A-za-z]{3,6}-[A-za-z]{3,6}-[A-za-z]{3,6}$" #Checks for colour-COLOUR-Colour pattern
            if (not re.match(pattern, value)):
                error="Please enter using the correct format"
                raise TypeError("Input does not match format")
            elif (not(colour_checker(value))): #Checks that colours are spelled correctly/the input is correct
                error="Check that colours are spelled correctly"
                raise TypeError("Input does not match format")
            return value
        except:
            print(error)
def colour_checker(string): #Checks if the colours input exist in the list
    resistors = string.split("-") #Splits string into array
    for resistor in resistors:
        resistor=resistor.lower()
        if resistor not in colours: 
            return False
    return True  
def resistance(string): #Converts the colours into the resistance value
    resistors = string.split("-") #Splits string into array
    nums = [] #empty array
    for resistor in resistors:
        resistor=resistor.lower()
        nums.append(colours.index(resistor))#Uses index to get number
    return float(int(str(nums[0])+str(nums[1]))*(10**nums[2])) #converts numbers into ohms with concatination and multiplication
print("A resistor colour code looks like this: Colour-Colour-Colour")
user_colours = err_input("Please enter your resistor colour code: ")
print("You entered: " + user_colours)
print("The value of the resistor is: " + str(resistance(user_colours)) + " ohms")

