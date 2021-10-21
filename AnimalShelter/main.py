from animal_shelter import AnimalShelter

def err_input(msg, limits=[None,None], error="Error, please try again"): #Takes user input and throws/handles errors 
    while(True):
        try:
            value=int(input(msg))#Stores input
            err1=value<limits[0] if limits[0]!=None else False #Checks if smaller than min
            err2=value>limits[1] if limits[1]!=None else False #Checks if larger than max
            if (err1 or err2):#only takes input within limit
                raise ValueError
            return value
        except ValueError:
           print(error)
#Generate an animal shelter called the ospca
ospca=AnimalShelter(err_input("How many dogs would you like to start with in the shelter? (0-10): ",[0,10]))
while True:
    print ()
    print ("Hello operator, what will you do?")
    print ("1 - Display dogs")
    print ("2 - Add a dog")
    print ("3 - Remove a dog")
    print ("4 - Display shelter costs")
    print ("5 - Exit shelter")
    choice = err_input("Choose an option (1-5): ",[1,5])
    if (choice==1):# display list of dogs
        print(ospca)
    elif (choice==2):# add a dog object
        name=input("Input the dogs name: ")
        breed=input("Input the dogs breed: ")
        age=err_input("Input the dogs age: ", [0, None])
        ospca.add_dog(name, breed, age)
    elif (choice==3):# remove a dog object
        print(ospca)
        choice=err_input("Type the number of the dog you wish to remove: ", [1, ospca.get_num_dogs()])-1
        print(ospca.get_dog(choice), end=" ")
        print("who is no longer in the shelter thanks to an adoptive family.")
        ospca.remove_dog(choice)
    elif (choice==4):# display the operating cost
        print(ospca.calculate_costs())
    elif (choice==5): #Quit
        print("\nGoodbye.")
        break