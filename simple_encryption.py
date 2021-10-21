#Name: Zac Waite
#Date: March 6 2021
#Program Name: simple_encryption.py
#Purpose: Encrypts and decrypts messages using a simple cypher
#Takes input with error handling, given the user message and optional error message
import random
def errInput(msg, limits, error="Error, please try again"): 
    while(True):
        try:
            value=int(input(msg))#Stores input
            if (value < limits[0] or value > limits[1]):
                raise TypeError("Integer out of Range")
            return value
        except:
            print(error)
def encrypt(direc, phrase, rot):
    answer = ""#Answer begins empty
    for i in range(len(phrase)): #Goes through each character
        unicode = ord(phrase[i]) #Converts to unicode
        if (unicode<=90 and unicode >=65): #Lowercase
            if (direc==1): #Encrypt
                unicode+=rot
                if (unicode>90): #Jumps letter gap
                    unicode+=6
            else: #Decrypt
                unicode-=rot
                if (unicode<65): #Jumps letter gap
                    unicode+=58
        elif (unicode>=97 and unicode<=122): #Uppercase
            if (direc==1): #Encrypt
                unicode+= rot
                if(unicode>122): #Jumps letter gap
                    unicode-=58
            else: #Decrypt
                unicode-=rot
                if(unicode<97): #Jumps letter gap
                    unicode-=6
        elif (unicode==32): #Space
            pass
        else: #Special Character
            print("Error Encrypting - some characters will be unchanged")
        answer+=str(chr(unicode)) #append new char
    return answer
print("This program will encrypt or decrypt a phrase using the")
print("simple encryption method of rotating the letters")
phrase = input("Enter a phrase (No special characters): ")#User inputs word
num = errInput("Enter rotation amount (0-32 [0 = random]): ", [0,32])#User inputs rotation
if (not num): #0
    num = random.randint(1, 32)
print("1: Encrypt")
print("2: Decrypt")
choice = errInput("Enter your choice (1-2): ", [1,2])#User inputs rotation
newPhrase = encrypt(choice, phrase, num) #Encrypts/decrypts
print("Input: " + phrase)
print("Ouput: " + newPhrase)
