# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

def getAmountApplePrice():
    amountMoney = int(input("How much money do you have? "))
    appPrice = int(input("What is the price of an apple per piece? "))
    return amountMoney, appPrice

def getNappleChange(amount, applePrice):
    Napple = int(amount//applePrice)
    change = amount % applePrice
    return Napple, change

amount, applePrice = getAmountApplePrice()
Napple, change = getNappleChange(amount, applePrice)

print(f"You can buy {Napple} apples and your change is {change:.2f} pesos.")