#Name: Zac Waite
#Date: March 29 2021
#Program Name: sorters.py
#Purpose: Sort lists with different algorithms

import math
import random

def err_input(msg, limits=None, error="Error, please try again"): #Takes user input and throws/handles errors 
    while(True):
        try:
            value=int(input(msg))#Stores input
            if(limits):
                if (value < limits[0] or value > limits[1]):#only takes input within limit
                    error="Please use the options provided"
                    raise TypeError("Integer out of Range")#throws error
            return value
        except:
            print(error)

def sel_sort(data, sm_lg=True):
    for i in range (0,len(data)-1):
        smallest = i #Start at new lowest value each time, incrementally bigger
        for index in range (i+1,len(data)): #for each index in the list, 
            size_comp=(data[index]<data[smallest]) if sm_lg else (data[index]>data[smallest]) #If the value is smaller/bigger (based on input),
            if (size_comp): data[index],data[smallest]=data[smallest],data[index] # Swap values with smallest
def bub_sort(data, sm_lg=True):
    for a in range(len(data)):#  loop to control number of passes
        for b in range(0,len(data)-1):#  loop to control number of comparisons for length of list-1
            size_comp=(data[b]>data[b+1]) if sm_lg else (data[b]<data[b+1]) #If the next value is bigger (Or smaller, depending on parameters)
            if (size_comp): data[b],data[b+1]=data[b+1],data[b] #Flip the value with the one after it.
def ins_sort(data, sm_lg=True):
    for i in range (1, len(data)): 
        item = data[i] #Store a value to add back in later
        move_item = i #Store value of i that can be iterated
        size_comp=(data[move_item-1]>item) if sm_lg else (data[move_item-1]<item) #If the listed value is bigger (Or smaller) than the stored value 
        while (move_item > 0 and size_comp): #Make sure the start of the list hasn't been reached (And check above)
            data[move_item] = data[move_item - 1] #(The data item is equal to the one before it)
            move_item -= 1 #Move to the previous item on the list
            size_comp=(data[move_item-1]>item) if sm_lg else (data[move_item-1]<item) #Re-check bigger/smaller compared to stored value
        data[move_item]=item
def format(content, prefix="", cols=0, rows=0):#Over kill print formatting function from previous project, using it again because why not
    cells=cols*rows #Num of cells is column times rows
    cellements=len(content) #Number of cells with elements is just len of content
    if (not cells): 
        if (not rows and cols): #If only rows is defined, calculate cols
            rows=(len(content)//cols)
            if (len(content)%cols!=0):
                rows+=1
        elif(not cols and rows): #If only cols is defined, calcualte rows
            cols=(len(content)//rows)
            if (len(content)%rows!=0):
                cols+=1
        else: #If neither rows nor cols is defined, make a square(ish)
            cols=math.ceil(math.sqrt(len(content)))
            rows=(len(content)//cols)
            if (len(content)%cols!=0):
                rows+=1
    table=[] #empty table
    row=[] #Empty row that will fill, input to table, and then empty
    max_width=0 # max width for a cell, so that all cells stay the same size
    for a in range(rows): #go through each row
        row=[]
        for b in range(cols): #go through each column in row
            if (a*cols+b>cellements-1): #If there is no cellement left, stop
                break
            if (not len(prefix)): #No prefix added, add the content to the row
                row.append(str(a*cols+b) + ": " + str(content[a*cols+b]))
            else: #Prefix added, add content to the row
                row.append(str(a*cols+b) + ": " + str(prefix) + str(content[a*cols+b]))
            if (len(row[-1])>max_width): #New max width if one is bigger
                max_width=len(row[-1])
        table.append(row) #Adds row to table
    width=(max_width+3)*cols+1 #Width is the cell width+3 by the number of cells, plus 1
    print("-"*width) #prints ------
    for a in range(len(table)): #prints each row
        width=(max_width+3)*len(table[a])+1 #finds new width for each row
        print("|", end="") #print start of the line
        for b in range(len(table[a])): #prints each cell
            print(" " + table[a][b].ljust(max_width) + " |", end="")
        print("\n" + "-"*width) #prints end of the line

sorters=["Selection Sort", "Bubble Sort", "Insertion Sort"] #User's options for sorting
orders=["Ascending", "Decending"] #User's options for order

while (True):
    num_nums=err_input("How many numbers would you like to generate?: ") #Get number of numbers to generate from user
    nums=[] #Empty array for numbers
    for i in range(num_nums):
        nums.append(random.randint(0,1000)) #Append random numbers from 0-1000
    print("The unsorted list is:")
    print(nums)
    format(sorters) #Prints sorting options with table making function
    sorter=err_input("What type of sort would you like to perform? (0-2): ", [0,2]) #User inputs chosen sorter 
    format(orders) #Prints order options with table function
    order=err_input("In what order would you like it sorted? (0-1) ", [0,1]) #User inputs chosen order
    if sorter==0: sel_sort(nums, not order) #If they choose 0, run selection sort
    elif sorter==1: bub_sort(nums, not order) #1, run bubble sort
    elif sorter==2: ins_sort(nums, not order) #2, insertion sort
    print("\nPerforming", sorters[sorter])
    print("The sorted list is:")
    print(nums)
    repeat=input("Would you like to run again? (y/n): ") #User indicated if they want to run the program again
    if (not(repeat=="y" or repeat=="Y")):
        break #If they don't type y, break the while loop. 