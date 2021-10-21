#Name: Zac Waite
#Date: March 22 2021
#Program Name: Fibonacci.py
#Purpose: Determines the nth fibonacci number

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
def fibo (n):
    if (n==0): #case of 0
        return 0
    elif (n==1 or n==2): #base cases of 1 and 2
        return 1
    else:
        return fibo(n-1)+fibo(n-2) #returns the two numbers before it added together.
def example (n):
    nums = [1] #stores fibo numbers
    num1 = 1 #stores earlier fibo number
    num2 = 1 #stores current fibo number
    for i in range(n):
        nums.append(num2)
        num2=num1+num2 #generates fibo numbers and appends then to display
    print("The first Fibonacci numbers are listed as follows:")
    print(str(nums)[1:len(str(nums))-1], "...") #displays fibo example numbers
example(9)
n1= err_input("What Fibonacci term would you like to see (0-100): ", [0, 100])
print("Element", n1, "of the fibonacci sequence is", fibo(n1))
