#Name: Zac Waite
#Date: March 18 2021
#Program Name: hangman.py
#Purpose: Plays a game of hangman

import math
import random

def err_input(msg, error="Error, please try again"): #Takes user input and throws/handles errors 
    while(True):
        try:
            value=str(input(msg))#Stores input
            if len(value)!=1 or (not ((ord(value)>=65 and ord(value)<=95) or (ord(value)>=97 and ord(value)<=122))): #Makes sure it is a letter
                error="Please enter a single letter"
                raise TypeError("Letter not entered")#throws error
            return value
        except:
            print(error)
hangman=[[" ", "O", " "], #Hangman template
         ["/", "|", "\\"],
         [" ", "|", " "],
         ["/", " ", "\\"]
          ]
hangedman=[[" ", "", " "], #Blank hangman
         ["", "", ""],
         [" ", "", " "],
         ["", " ", ""]
          ]
def hanged (): #Adds to hangman until dead, then returns true
    one=False #Stops after one letter is different
    for a in range(len(hangman)):
        if not one:
            for b in range(len(hangman[a])):
                if hangedman[a][b]!=hangman[a][b]: #If one character is different, change it, then exit.
                    hangedman[a][b]=hangman[a][b]
                    one=True
                    break
        else:
            break
    if(not one): #If the hangman is dead, return true
        return True
    return False

school=['Teacher', 'Pencil', 'Black Board'] #School words
restaurant=['Dinner Table', 'Salad Menu', 'Cutlery'] #Restaurant words
grocery_store=['Clean up on Aisle', 'Cashier', 'Bakery'] #Grocery store words
beach = ['Sandy Feet', 'Umbrella', 'Sunshine'] #beach words
house = ['Garage', 'Couch Pillow', 'Windows'] #house words
categories=['School', 'Restaurant', 'Grocery Store', 'Beach', 'House'] #category words
words=[school, restaurant, grocery_store, beach, house] #category word 2d list

won=False #Variables for won and lost
lost=False
num1 = random.randint(0, len(words)-1)  #Random number to select category
num2 = random.randint(0, len(words[num1])-1) #Random number to select word
category = categories[num1]
word = words[num1][num2].upper() #Get the uppercase letter
split_words = word.split() #Splits words 
hidden_text=[]
for split_word in split_words:
    hidden_text.append("-"*len(split_word))#Hidden text is made up of lines and spaces
hidden_word = " ".join(hidden_text)
num_words = len(word.split()) #Number of words

while(not won and not lost):
    print("Category: " + category)
    print("Number of Words: " + str(num_words))
    print(hidden_word)
    for a in range(len(hangedman)):
        for b in range(len(hangedman[a])):#Prints all hangman pieces
            print(hangedman[a][b],end="")
        print("")
    guess=err_input("Please enter a letter: ").upper() #Gets user input confirming proper input
    indexes=[]
    if (guess in word):
        print("Correct")
        indexes = [i for i, char in enumerate(word) if char==guess] #List comprehension to get all indexes  
        for index in indexes:
            hidden_word=hidden_word[:index]+word[index]+hidden_word[index+1:] #Adds new character instead of space
        if word==hidden_word: #IF the word is done, you have won
            won=True
            print("The word was " + hidden_word)
    else:
        print("Incorrect")
        if(hanged()): #If it is hanged, you lose
            lost=True
            print("The man has been hanged")
    print("")
if won:
    print("Congratulations!")
elif lost:
    print("You lose")
        
