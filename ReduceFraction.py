#Name: Zac Waite
#Date: March 22 2021
#Program Name: ReduceFraction.py
#Purpose: Reduces a fraction to a smaller number

def err_input(msg, error="Error, please try again"): #Takes user input and throws/handles errors 
    while(True):
        try:
            value=int(input(msg))#Stores input
            return value
        except:
            print(error)
def gcd (a,b): #finds greatest common divisor of 2 numbers
    if (b==0): #base case of 0
        return a
    else:
        return gcd(b, a%b) #flips numbers and takes modulus
num = err_input("What is the numerator of your fraction?: ")
den = err_input("What is the denominator of your fraction?: ")
factor = gcd(num,den) #Finds common factor
if (factor==1):
    print("The fraction can not be reduced, it is " + str(num) + "/" + str(den))
else:
    new_num=num//factor #Finds new numerator
    new_den=den//factor #Finds new denominator
    print("The fraction "+str(num)+"/"+str(den)+" can be reduced to "+str(new_num)+"/"+str(new_den)+".")
