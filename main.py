from menu import MENU, resources
from time import sleep


def insert_coins():
    quarters = 0.25 * float(input("How many quarters ($0.25)? "))
    dimes = 0.1 * float(input("How many dimes ($0.1)? "))
    nickles = 0.05 * float(input("How many nickles ($0.05)? "))
    pennies = 0.01 * float(input("How many pennies ($0.01)? "))
    return quarters + dimes + nickles + pennies


def check_resources(drink_type):
    if check_water(drink_type) == 1 and check_coffee(drink_type) == 1 and check_milk(drink_type) == 1:
        return 1
    # simpler way:
    # for item in drink_type['ingredients']:
    #     if drink_type[item] > resources[item]:
    #         print(f"Sorry, there's not enough {item}")
    #         return 0
    # return 1

def check_water(drink_type):
    if resources['water'] >= MENU[drink_type]['ingredients']['water']:
        return 1


def check_coffee(drink_type):
    if resources['coffee'] >= MENU[drink_type]['ingredients']['coffee']:
        return 1


def check_milk(drink_type):
    if 'milk' not in MENU[drink_type]['ingredients']:
        return 1
    elif resources['milk'] >= MENU[drink_type]['ingredients']['milk']:
        return 1


def deduct(drink_type):
    resources['water'] -= MENU[drink_type]['ingredients']['water']
    resources['coffee'] -= MENU[drink_type]['ingredients']['coffee']
    if 'milk' in MENU[drink_type]['ingredients']:
        resources['milk'] -= MENU[drink_type]['ingredients']['milk']

def animation(drink_type):
    print(f"Preparing {drink_type}")
    for i in range(5):
        print(".", end='')
        sleep(0.6)
    print(f"\nHere is your {drink_type} ☕️. Enjoy!")

def make_coffee(drink_type):
    global CASH
    if check_resources(drink_type) == 1:
        print(f"{drink_type}: insert ${MENU[drink_type]['cost']} ")
        total_coins = round(insert_coins(), 2)
        if total_coins == MENU[drink_type]['cost']:
            deduct(drink_type)
            CASH += MENU[drink_type]['cost']
            animation(drink_type)
        elif total_coins > MENU[drink_type]['cost']:
            change = round(total_coins - MENU[drink_type]['cost'], 2)
            print(f"Here is ${change} in change.")
            deduct(drink_type)
            CASH += MENU[drink_type]['cost']
            animation(drink_type)
        else:
            print(f"You inserted ${total_coins} and {drink_type} costs ${MENU[drink_type]['cost']}. It's not enough")
    else:
        print("Not enough resources")


def service():
    print(f"Water: {resources['water']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Money: ${CASH}")

def refill():
    service()
    print("=== R E F I L L ===")
    resources['water'] += int(input("How many ml of water? "))
    resources['coffee'] += int(input("How many g of coffee? "))
    resources['milk'] += int(input("How many ml of milk? "))

is_working = True
# main cash container
CASH = 0

while is_working == True:
    task = input("What would you like? (espresso/latte/cappuccino): ")
    if task == "espresso" or task == "latte" or task == "cappuccino":
        make_coffee(task)
    elif task == "report":
        service()
    elif task == "off":
        is_working = False
    elif task == "refill":
        refill()
    else:
        # make_coffee(task)
        print("Command not recognised, try again")

