import menu

waterLeft = {menu.resources['water']}
milkLeft = {menu.resources['milk']}
coffeeLeft = {menu.resources['coffee']}

prompt = input ("What would you like? (espresso/latte/cappuccino): ")
# if prompt == 'off':
#     # TODO: turn off machine
# elif prompt == 'report':
#     print (resources)
# elif (prompt == 'espresso' or prompt == 'latte' or prompt == 'cappuccino'):
waterNeeded = menu.MENU['prompt']['ingredients']['water'] # if not off/report
milkNeeded = menu.MENU['prompt']['ingredients']['milk']
coffeeNeeded = menu.MENU['prompt']['ingredients']['coffee']
costPerCup = menu.MENU['prompt']['cost']
#else:
#print ("Wrong input. Please enter again.")
# restart (execute again)

resoourceRequired = 'none'
if (waterLeft-waterNeeded) <= 0:
    resoourceRequired = 'water'
if (milkLeft-milkNeeded) <= 0:
    resoourceRequired = 'milk'
if (coffeeLeft-coffeeNeeded) <= 0:
    resoourceRequired = 'coffee'

if (resoourceRequired == 'none'):
    coinsValue = 0.0
    print ("Please enter coins. Enter \"done\" when completed")
    while (coinsValue >= costPerCup):
        coinType = input ("Coin: ")
        coinType.lower()
        if (coinType == 'quarter'):
            coinsValue += 0.25
        elif (coinType == 'dime'):
            coinsValue += 0.10
        elif (coinType == 'nickle'):
            coinsValue += 0.05
        elif (coinType == 'penny'):
            coinsValue += 0.25
        elif (coinType == 'done'):
            print ("Sorry. That's not enough money. Money refunded.")
            break
        else:
            print ("Wrong input. Please enter again.")
    
else:
    print (f"Sorry. There is not enough {resoourceRequired}.")


