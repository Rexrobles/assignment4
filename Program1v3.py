# Create a program that will ask for name, age and address. 
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____ .

def getNameAgeAddress():
    name_ = input("Name: ")
    age_ = int(input("age "))
    address_ = input("address: ")
    return name_ ,age_ ,address_

def display(name, age, address):
     print(f"hi my name is {name}. I am {age} years old and I live in {address}")

#step 1
# ask for name, age and address

name, age, address = getNameAgeAddress()

# 2. display
display(name, age, address)