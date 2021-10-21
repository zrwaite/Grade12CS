#Name: Zac Waite
#Date: March 22 2021
#Program Name: NChooseR.py
#Purpose: Finds answer to NcR equation for grouping 

def err_input(msg, limits, error="Error, please try again"): #Takes user input and throws/handles errors 
    while(True):
        try:
            value=int(input(msg))#Stores input
            if (value < limits[0] or value > limits[1]):#only takes input within limit
                error="Select a number in the correct range"
                raise TypeError("Integer out of Range")#throws error
            return value
        except:
            print(error)
def fact (n): #finds factorial of a number
    if (n==0 or n==1): #base case of 0 or 1
        return 1
    else:
        return n*fact(n-1) #returns n times the number below it factorial
def eff_fact (n, n2, big_num): #Efficient factorial uses past factorials to reduce calculations
    if (n==n2): #Once n reaches a previously calcualted n, just use a previous factorial
        return big_num
    else: 
        return n*eff_fact(n-1, n2, big_num) #Returns n times the factorial before it
def ncr (n, r):
    if r>n-r: #To be more efficient, calculates smallest to biggest and uses eff_fact
        small_den=fact(n-r) #Small denominator
        big_den=eff_fact(r, n-r, small_den) #Big denominator uses small_den with eff_fact
        num=eff_fact(n, r, big_den) #Numerator uses big_den with eff_fact
    else: #Repeats above in different order, to remain smallest to biggest
        small_den=fact(r)
        big_den=eff_fact(n-r, r, small_den)
        num=eff_fact(n, n-r, big_den)
    return int(num/(small_den*big_den)) #calculates proper ncr
print("This program will calculate the number of ways to choose \nr different objects from a set of n objects")
r = err_input("How many objects would you like to choose? (0-100): ", [0,100])
n = err_input("how many objects are there to choose from? (" + str(r) + "-100): ", [r,100])
print("There are",ncr(n,r),"ways to choose",r,"objects from a set of",n,"objects.")
