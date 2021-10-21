#Name: Zac Waite
#Date: March 6 2021
#Program Name: palindrome1.py
#Purpose: Determines if a string is a palindrome
#Takes input with error handling, given the user message and optional error message
def errInput(msg, error="Error, please try again"): 
    while(True):
        try:
            value=str(input(msg))#Stores input
            return value
        except:
            print(error)
print("Palindromes are words that are the same forwards and backwards")
print("This program determines if a word is a palindrome")
word = errInput("Enter a word: ")#User inputs word
length = len(word)#Length of word
revWord = ""#Word in reverse starts empty
lowWord = word.lower()#Lowercase word
half=False#Used to stop cheking palindrome at the halfway point (more efficient)
answer = "is"#Answer defaults to is, becomes is not
for i in range(length):
    revWord+=str(word[length-i-1])#Adds end value to start
    if (not half): 
        if (i>length//2+length%2):#If past the halfway point of the string, this is inefficient
            half=True
        elif(lowWord[i]!=lowWord[length-i-1]):#If not a palindrome, indicate so, and stop checking
            answer += " not"
            half=True
print(word + " in reverse is " + revWord)
print("It " + answer + " a palindrome")
