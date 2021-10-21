#Name: Zac Waite
#Date: March 18 2021
#Program Name: fund_raising.py
#Purpose: Calculates fundraising data based on input
'''As you will see I definitely had a lot of fun with this assignment - it took me extra time but I
think it was worth it, I can use these functions in the future for sure- hopefully the delay of my submissions will not affect my mark'''

import math
schools=["Catholic Central", "Holy Cross", "John Paul II", "Mother Teresa", "Regina Mundi", "St. Joseph", "St. Mary", "St. Thomas Aquinas","*Exit*",] #list of schools
donations=[.25,.5,1,2]# List of donation amounts
final=[["School:", "Donation:", "Students:", "Total:"]]
def err_input(msg, limits, error="Error, please try again"): #Takes user input and throws/handles errors 
    while(True):
        try:
            value=int(input(msg))#Stores input
            if (value < limits[0] or value > limits[1]):#only takes input within limit
                error="Please use the options provided"
                raise TypeError("Integer out of Range")#throws error
            return value
        except:
            print(error)

def one_d_formatter(content, prefix="", cols=0, rows=0):#This might be overkill but this function automatically formats lists in a nice way
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


def two_d_formatter(content):#Once again might be overkill but this function automatically formats 2d lists in a nice way
    rows=len(content) #rows is the 2d array row value
    cols=0 # cols are calculated to largest value, in case of missing values in certain rows
    for a in range(rows):
        if (len(content[a])>cols):
            cols=len(content[a])
    table=[] #Emtpy table
    row=[] #Empty row to add to table and reset
    widths=[] #Different widths for each column
    for a in range(rows): #go through each row
        row=[]
        for b in range(cols): #go through each column
            if (a*cols+b>len(content*cols)-1): #if no cellements left, stop
                break
            row.append(str(content[a][b])) #add content to cell of row
            if (a==0): #Creates new elements in widths
                widths.append(len(str(content[a][b])))
            else:
                if (widths[b]<len(str(content[a][b]))): #increases widths values to max
                    widths[b]=len(str(content[a][b]))
        table.append(row) #Adds row to table
    width=0#Width of whole table
    for i in range(len(widths)): #adds up widths of columns
        width+=widths[i]+3
    width+=1
    print("-"*width) #prints -------
    for a in range(len(table)):
        print("|", end="") #starts new line
        for b in range(len(table[a])):
            print(" " + table[a][b].ljust(widths[b]) + " |", end="") #prints content
        print("\n" + "-"*width) #ends line
kill=False #controls if program is running
while (not kill):
    for a in range(1, len(schools)-1): #goes through each school, but not exit
        one_d_formatter(schools) #Shows schools remaining
        choice=err_input("Please choose a school: ", [0,len(schools)-1]) #Takes user input for school
        if (choice==len(schools)-1): #Ends program
            kill=True
            break
        final.append([schools[choice]]) #Adds schools to final list
        del schools[choice] #Deletes school from initial list
        one_d_formatter(donations, "$") #Shows donation options
        choice=err_input("What is their donation amount: ", [0,len(donations)-1]) #Gets user input on donation amount
        final[a].append(donations[choice]) #Adds donation to final list
        choice=err_input("How many students are at that school: ", [0, 100000]) #Gets user input on students
        final[a].append(choice) #Adds students to final list
        final[a].append("$" + str(final[a][1]*final[a][2])) #Adds total quantity to final list
    if (kill):
        break
    total=0
    for i in range(1,len(final)): #Finds total
        total+=float(final[i][3].split("$")[1])
    final.append(["Total:", "", "", "$"+str(total)])
    two_d_formatter(final) #Outputs final result
    '''
    I chose to use a different format than you did in the video, becuase you said it was a suggestion,
    and I believe that while my way took more work the output I have is more compressed while containing more
    information.
    '''
    kill=True
print ("Thanks for using the Donation Estimator")      
        
