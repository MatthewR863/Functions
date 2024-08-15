# Name: Matthew Reynolds # Date: 03/14/2024
# Class: Comp 163 #Section:002

# Description: Making a program that reads a list of integers

# To see if the numbers are multiples of 10
def is_list_mult10(mylist):
    return all(x % 10 == 0 for x in mylist)

# To see if the numbers aren't multiples of 10
def is_list_no_mult10(mylist):
    return all(x % 10 != 0 for x in mylist)

# Inputs
def run_list_multi():
    mylist = []
    num_items = int(input("Enter size of the list: "))
    for i in range(num_items):
        item = int(input(f"Enter item {i + 1}: "))
        mylist.append(item)

    # Output
    if is_list_mult10(mylist):
        print("all multiples of 10")
    elif is_list_no_mult10(mylist):
        print("no multiples of 10")
    else:
        print("mixed values")

run_list_multi()

