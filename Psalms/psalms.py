#Name: Zac Waite
#Date: March 28 2021
#Program Name: psalms.py
#Purpose: Reduces a fraction to a smaller number
import re
import math
def err_input(msg, error="Error, please try again"): #Takes user input and throws/handles errors 
    while(True):
        try:
            value=int(input(msg))#Stores input
            return value
        except:
            print(error)
def b_s(array,item): #binary search takes array and search item
    left=0 #non-recursive b_s means left is always 0 at the start
    right=len(array) #non-recursive b_s means right is always len(array)
    while(left<=right): #until whole array has been searched
        print("Searching array:", end=" ") 
        print(array[left:right+1], 'for', item, '-', len(array[left:right+1]), 'items remaining') #print info about search
        middle=int((left+right)/2)#middle becomes average of two outer search points
        if (array[middle]==item): #If item is found, leave loop
            break
        elif (item<array[middle]): #If item is smaller than current search value, move the max size to one less than the search value 
            right=middle-1
        else:
            left=middle+1 # If item is bigger than current search value, move the min size to one more than the search value
    if (left>right):
        return False #If left is greater than right, the whole array was searched, so return false
    else:
        return True #If not, the loop broke, so return true

psalms_nums=[] #Nums of psalms
psalms_list={} #Dictionary to store the text psalms with their index values
psalms_file=open("Psalms.txt", "r") #Open file

while(True):
    try:
        key=int(re.sub('\\n', '', psalms_file.readline())) #key of dictionary is integer given in text file
        psalms_nums.append(key) #add key to key list
    except ValueError: #If integer can't be created, file is bad or end of list. Either way, break. 
        break
    value=re.sub('\\n', '', psalms_file.readline()) #value of dictionary is next line. 
    psalms_list.update({key:value}) #create dictionary pair
psalms_file.close() #close file
psalms_nums.sort() #Just in case, sort before a binary search on inputted information
index=err_input("What psalms number are you looking for?: ")
if(b_s(psalms_nums, index)): #If binary search for user inputted value returns true, print psalsm that was found. Else, tell user nope.
    print("Here is the title of psalm " + str(index) + ":")
    print(psalms_list[index])
else:
    print("That psalm was not found, sorry")
