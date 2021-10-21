#Name: Zac Waite
#Date: March 6 2021
#Program Name: palindrome3.py
#Purpose: Determines if a phrase is a palindrome
#Takes input with error handling, given the user message and optional error message
def errInput(msg, error="Error, please try again"): 
    while(True):
        try:
            value=str(input(msg))#Stores input
            return value
        except:
            print(error)
print("Palindromes are words that are the same forwards and backwards")
print("This program determines if a phrase is a palindrome")
word = errInput("Enter a phrase: ")#User inputs word
length = len(word)#Length of word
revWord = ""#Word in reverse starts empty
answer = "is"#Answer defaults to is, becomes is not
for i in range(length):
    revWord+=str(word[length-i-1])#Adds end value to start
compWord = "".join(word.split()) #Deletes all spaces
lowWord = compWord.lower()#Lowercase word
length=len(compWord)#New length definition
for i in range(length):
    if (i>length//2+length%2):#If past the halfway point of the string, this is inefficient
        break
    elif(lowWord[i]!=lowWord[length-i-1]):#If not a palindrome, indicate so, and stop checking
        answer += " not"
        break
print(word + " in reverse is " + revWord)
print("It " + answer + " a palindrome")
