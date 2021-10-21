#Name: Zac Waite
#Date: March 23 2021
#Program Name: cancer.py
#Purpose: Detects abnormal blobs from a textfile

def chemo(row,col): #Gets rid of cancer spot
  if cancer[row][col] == "-": #If cancer is detected, 
    cancer[row][col] = " "    #change it to a blank
    chemo(row - 1, col - 1)   #Then look all around that element
    chemo(row - 1, col)
    chemo(row - 1, col + 1)
    chemo(row, col - 1)
    chemo(row, col + 1)
    chemo(row + 1, col - 1)
    chemo(row + 1, col)
    chemo(row + 1, col + 1)
def biopsy(line): #Detects if there is "cancer" in a line of text
    if "-" in line:
        loc = line.index("-") #location is the index of the cancer
        chemo(i, loc) #Performs chemo on the cancer
        global cancer_cells
        cancer_cells+=1 #Adds to cancer cells
        biopsy(line) #Recurses a biopsy on the rest of the line
cancer_cells=0 #Counts number of cancer cells or blobs
cancer_file=open("cancer.txt", "r") #Open file
cancer=cancer_file.readlines() #Read file as an array of lines
cancer_file.close() #Close file
print("Your cancer date file looks like:")
for i in range(len(cancer)):
    print(cancer[i], end="") #prints out cancer
    cancer[i]=list(cancer[i]) #converts string to list
for i in range(len(cancer)):
    biopsy(cancer[i]) #Checks each line for cancer
if cancer_cells: #If cancer is detected
    print("\n\nYour file had", cancer_cells, "cancer spots in it.")
    print("The new grid is:")
    for line in cancer: 
        line="".join(line) #For each line, rejoin array as string
        print(line, end="")#and print it out
else: #No cancer is detected
    print("No cancer spots were detected in your file")
