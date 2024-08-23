import menu
from sys import exit

profit = round(0.0, 2)

def printReport ():
    global profit
    print (f"Water: {menu.resources['water']}")
    print (f"Milk: {menu.resources['milk']}")
    print (f"Coffee: {menu.resources['coffee']}")
    print (f"Money: ৳ {profit}")

def placeOrder (water, milk, coffee, coins, cost):
    global profit
    menu.resources['water'] -= water
    menu.resources['milk'] -= milk
    menu.resources['coffee'] -= coffee
    profit += cost
    refund = coins - cost

    print ()
    if (refund>0):
        print (f"Here's your ৳ {round(refund, 2)} in change.")
    print (f"Enjoy your coffee. ")

def checkAndOrder():
    waterLeft = menu.resources['water']
    milkLeft = menu.resources['milk']
    coffeeLeft = menu.resources['coffee']

    waterNeeded = menu.MENU[prompt]['ingredients']['water']
    if ('milk' in menu.MENU[prompt]['ingredients']):
        milkNeeded = menu.MENU[prompt]['ingredients']['milk']
    else: milkNeeded = 0
    coffeeNeeded = menu.MENU[prompt]['ingredients']['coffee']
    costPerCup = menu.MENU[prompt]['cost']

    resoourceRequired = 'none'
    if (waterLeft-waterNeeded) <= 0:
        resoourceRequired = 'water'
    if (milkLeft-milkNeeded) <= 0:
        resoourceRequired = 'milk'
    if (coffeeLeft-coffeeNeeded) <= 0:
        resoourceRequired = 'coffee'

    if (resoourceRequired == 'none'):
        coinsValue = round(0.0, 2)
        coinType = 'none'
        print ("Please enter coins. Enter \"done\" when completed")

        while (coinType != 'done'):
            print (f"Price: {round(costPerCup, 2)}")
            print (f"Balance: ৳ {round(coinsValue, 2)}")
            coinType = input ("Coin: ")
            coinType.lower()
            if (coinType == 'quarter'):
                coinsValue += 0.25
            elif (coinType == 'dime'):
                coinsValue += 0.10
            elif (coinType == 'nickle'):
                coinsValue += 0.05
            elif (coinType == 'penny'):
                coinsValue += 0.01
            elif (coinType == 'done'):
                continue
            else:
                print ("Wrong input. Please enter again.")

        if (coinsValue < costPerCup):
            print ("Sorry. That's not enough money. Money refunded.")
            exit()
        else:
            placeOrder(waterNeeded, milkNeeded, coffeeNeeded, coinsValue, costPerCup)

    else:
        print (f"Sorry. There is not enough {resoourceRequired}.")
        exit()

prompt = input ("What would you like? (espresso/latte/cappuccino): ")
if prompt == 'off':
    exit("Machine turned off.")
elif prompt == 'report':
    printReport()
elif (prompt == 'espresso' or prompt == 'latte' or prompt == 'cappuccino'):
    checkAndOrder()
else:
    exit("Wrong input. Start again.")