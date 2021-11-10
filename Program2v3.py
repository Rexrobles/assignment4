#Create a program that will ask how many apples and oranges you want to buy.
#Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
#Display the output in the following format.
#The total amount is ______.

def getNappleNorange():
    NumberofApple = int(input("How many apples do you want to buy? "))
    numberoforange= int(input("How many orange do you want to buy? "))
    return NumberofApple, numberoforange

def getprice(apple_number, orange_number):
     apple_price = apple_number * 20
     orange_prize = orange_number *25
     total = apple_price + orange_prize
     return total
 
Napples, Noranges = getNappleNorange()
totalPrice = getprice(Napples, Noranges)

print(f"The total amount is {totalPrice} pesos.")