#Name: Zac Waite
#Date: March 6 2021
#Program Name: palindrome2.py
#Purpose: Determines if a string contains palindromes
#Takes input with error handling, given the user message and optional error message
def errInput(msg, error="Error, please try again"): 
    while(True):
        try:
            value=str(input(msg))#Stores input
            return value
        except:
            print(error)
def pal(word): #Determines if a word is a palindrome
    length = len(word)#Length of word
    revWord = ""#Word in reverse starts empty
    lowWord = word.lower()#Lowercase word
    half=False#Used to stop cheking palindrome at the halfway point (more efficient)
    answer = True #Answer defaults to true, becomes false
    for i in range(length):
        revWord+=str(word[length-i-1])#Adds end value to start
        if (not half): 
            if (i>length//2+length%2):#If past the halfway point of the string, this is inefficient
                half=True
            elif(lowWord[i]!=lowWord[length-i-1]):#If not a palindrome, indicate so, and stop checking
                answer = False
                half=True
    return answer
print("Palindromes are words that are the same forwards and backwards")
print("This program determines if a sentence contains a palindrome")
sentence = errInput("Enter a sentence (Without punctuation): ")#User inputs sentence
words = sentence.split()#Splits sentence into individual words
pals = []#Empty array declaration
for word in words:
    if (pal(word)):#Goes through words and checks for palindromes, if so, adds to pals
        pals.append(word)
length=len(pals)#Length of array
if (not length):#No palindromes
    print("There are " + str(length) + " palindromes in this sentence")
elif (length==1):#One palindrome
    print("There is 1 palindrome in this sentence")
    print("It is: " + pals[0])
else:#Multiple palindromes
    print("There are " + str(length) + " palindromes in this sentence")
    print("They are: ", end="")
    for i in range(length):
        if (i==length-1):
            print(pals[i]) #prints without comma
            break
        print(pals[i] + ", ", end="") #prints with comma
