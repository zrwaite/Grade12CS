#Name: Zac Waite
#Date: March 18 2021
#Program Name: game_of_life.py
#Purpose: Plays John Conway's the game of life

import random
import math

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
def generate_grid(consistancy): #Creates the inititial grid such that life is spread out evenly
    c_index=consistancy #creates index for counting to each new point
    for a in range (grid_size):
        for b in range (grid_size):#Counts though rows and columns
            num=math.floor(c_index) #Take floor of number for integer comparisons
            if (num>=1):
                grid[a][b]=1 #Once the index passes 1, add life and subtract 1 from index
                c_index-=1
            c_index+=consistancy #Add the interval to the index
    for i in range(len(grid)): # print each row individually
        print(grid[i])
def print_grid(input_grid): #prints the grids fast
    grid_string="\n"
    for a in range (grid_size):
        for b in range (grid_size): #changes each list row and column into a string
            if (input_grid[a][b]):
                grid_string+="O"
            else: #Changes each element into O or .
                grid_string+="."
        grid_string+="\n"
    print(grid_string)
    if "O" not in grid_string:
        return False #In the meantime, checks for life since this is easier with string than in a list
    return True
def advance_generation(input_grid): #advances the generation one time
    '''
    This took me a while because python refuses to let me pass a list by value,
    even with .copy() or [:] slicing. Much easier in other languages.
'''
    coords=[] #Stores coordinates of changes that need to be made
    for a in range (grid_size):
        for b in range (grid_size):
            neighbours=0 #Everything down there just checks each point without going outside of the index, and adds to neighbours
            if a>0:
                neighbours+=input_grid[a-1][b]
                if b>0:
                    neighbours+=input_grid[a-1][b-1]
                elif b<grid_size-1:
                    neighbours+=input_grid[a-1][b+1]
            if a<grid_size-1:
                neighbours+=input_grid[a+1][b]
                if b>0:
                    neighbours+=input_grid[a+1][b-1]
                elif b<grid_size-1:
                    neighbours+=input_grid[a+1][b+1]
            if b>0:
                neighbours+=input_grid[a][b-1]
            elif b<grid_size-1:
                neighbours+=input_grid[a][b+1]
            if(input_grid[a][b]): #If there isn't 2-3 neighbours where there is life, it dies
                if not (neighbours==2 or neighbours==3):
                    coords.append([a,b,0])
            else: #If there are 3 neighbours near a point without life, there is now life.
                if (neighbours==3):
                   coords.append([a,b,1])
    for i in range(len(coords)): #Uses coordinates to make changes to original list since copy lists are annoying in python
        input_grid[coords[i][0]][coords[i][1]]=coords[i][2]
    return input_grid
                 
grid_size=20 #Current width of grid
grid=[] #Empty grid list
for i in range(grid_size):
    grid.append([0]*grid_size)#Adds 20 rows of 20 0s
generate_grid(err_input("Enter the amount of life cells to start with (>0, <400): ", [1, 399])/400.0) #Generates the grid from user input
print_grid(grid.copy())
generations=0 #Counts generations that have passed
while True: 
    loop=(err_input("How many generations would you like to generate (1-100): ", [1,100])) #Gets loop from user
    for i in range(loop):
        grid=advance_generation(grid.copy())#Advances the grid one generation
        generations+=1
        alive=print_grid(grid.copy()) #Prints grid and checks for life
        if not alive:
            break #leaves game of life if no more life
    if not alive:
        break
print("No life left after",generations,"generations")
