
# ********************
# Inventory.py
# ********************

#Object oriented class which initialises county, code, product, cost, quantity objects
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        # Shoe.__init__(country, code, product, cost, quantity)
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    #A string representation fo the above class. 
    def __str__(self):
        return f"{type(self).__name__}({self.country!r},{self.code!r}, {self.product!r}, {self.cost!r}, {self.quantity!r})"

    #Below function will work in conjunction with restock(shoe_list), this will add user input to quantity object
    def restock(self, amount):
        self.quantity += amount

    #This function multplies cost and quantity objects in shoe_list
    def value(self):
        return self.cost * self.quantity
    
    #This function returns code object in shoe_list and sum from value(self) function
    def value_info(self):        
        return self.code + " - " + str(self.value())

#Function reads txt file and appends all objects to shoe_list
def read_in_all_shoes(shoe_list):
    #this will allow first line of text file to not be read so the programme can perform tasks on numerical values
    with open ('inventory.txt', 'r') as myfile:
        for line in myfile: 
            line = line.split(",")
            shoe_object = Shoe(line[0], line[1], line[2], int(line[3]), int(line[4]))                              
            shoe_list.append(shoe_object)
            

#Will display all objects in shoe_list
def display_shoe_list(shoe_list):
    for shoe in shoe_list:
        print(shoe)

#Asks user to input each object in class and will append input to shoe_list
def add_shoe_to_list(shoe_list):
    country = input("What counrty:")
    code = input("What code:")
    product = input("What product:")
    cost = int(input("What cost:"))
    qty = int(input("What qty:"))
    shoe = Shoe(country, code, product, cost, qty)
    shoe_list.append(shoe)

#iterates through quantity in shoe_list and returns lowest value 
def find_shoe_with_lowest_qty(shoe_list):
    ret_val = shoe_list[0]
    for shoe in shoe_list:
        if shoe.quantity < ret_val.quantity:
            ret_val = shoe
    return ret_val

#iterates through quantity in shoe_list and returns highest value
def find_shoe_with_highest_qty(shoe_list):
    ret_val = shoe_list[0]
    for shoe in shoe_list:
        if shoe.quantity > ret_val.quantity:
            ret_val = shoe
    return ret_val

#Returns find_shoe_with_highest_qty function 
def print_sale_item(shoe_lsit):
    print("SALE!!!! ", find_shoe_with_highest_qty(shoe_list))

#prints shoe with lowest qty, and allows user to add to qty with restock() function
def restock(shoe_list):
    shoe_with_lowest_qty = find_shoe_with_lowest_qty(shoe_list)
    print("Lowest qty shoe is", shoe_with_lowest_qty)
    shoe_with_lowest_qty.restock(int(input("How many to add?")))

#Takes code object as user input, iterates through shoe_list and returns object with code object in. 
def search_shoe(shoe_list):
    search_code = input("enter code:")
    for shoe in shoe_list:
        if search_code == shoe.code:
            print(shoe)

#Function iterates through shoe_list and and total of value() function each time. Fucntion returns total of each line of object. and returns total of of all value of shoes. 
def display_shoe_values(shoe_list):
    total = 0
    for shoe in shoe_list:
        total += shoe.value()
        print(shoe.value_info())
    print("------------------")
    print("Total -", total)

print("Start")

#Belw function appends txt file to shoe_list
shoe_list = []
read_in_all_shoes(shoe_list)

#Menu defned below
running = True
while running:
    print()
    print("Please select")
    print(" a: add new shoe")
    print(" d: display shoe list")
    print(" v: display shoe values")
    print(" r: restock")
    print(" s: search")
    print(" o: print sale")
    print(" q: quit")
    user_selection = input("Select option:")

    if user_selection == "q":
        running = False
    elif user_selection == "d":

        #function will display list of shoes
        display_shoe_list(shoe_list)
    elif user_selection == "a":

        #Function allows user to add to list. 
        add_shoe_to_list(shoe_list)
    elif user_selection == "r":

        #Function allows user to update lowest qty of shoe. 
        restock(shoe_list)
    elif user_selection == "s":

        #Function will search shoe list by code object in class. 
        search_shoe(shoe_list)
    elif user_selection == "v":

        #Function will display all shoe values for each line in shoe_list
        display_shoe_values(shoe_list)
    elif user_selection == "o":
        
        #Will print highest qty shoe object in shoe_list
        print_sale_item(shoe_list)


print("end")
















