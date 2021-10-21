from cell_phone import CellPhone

def err_input(msg, limits=[None,None], error="Error, please try again"): #Takes user input and throws/handles errors 
    while(True):
        try:
            value=float(input(msg))#Stores input
            err1=value<limits[0] if limits[0]!=None else False #Checks if smaller than min
            err2=value>limits[1] if limits[1]!=None else False #Checks if larger than max
            if (err1 or err2):#only takes input within limit
                raise ValueError
            return value
        except ValueError:
           print(error)

p1 = CellPhone() #Generates random cell phont
print("Phone 1:")
print("Carrier = " + p1.get_carrier()) #Uses getter to print carrier
print("Type of phone = " + p1.get_type()) #Uses getter to print Type
print("Speed of phone = " + str(p1.get_speed()) + "Ghz") #Uses getter to print speed
print("Memory = " + str(p1.get_memory()) + "Gb") #Uses getter to print memory
print("Number of Apps = " + str(p1.get_num_apps()) ) #Uses getter to print num apps
print("\nGenerate a new cellphone:")
p2=CellPhone( #User inputs to create an object
    input("Input the cellphone carrier: "), 
    input("Input the cellphone type: "),
    err_input("Input the speed of the phone in GHz: ", [0, None]), 
    err_input("Input the memory of the phone in GB: ", [0, None]), #Must be at least 0
    err_input("Input the number of apps on the phone: ", [0, None])
)
print("\nPhone 2:") #Once again uses getters to print phone information
print("Carrier = " + p2.get_carrier())
print("Type of phone = " + p2.get_type())
print("Speed of phone = " + str(p2.get_speed()) + "Ghz")
print("Memory = " + str(p2.get_memory()) + "Gb")
print("Number of Apps = " + str(p2.get_num_apps()) )