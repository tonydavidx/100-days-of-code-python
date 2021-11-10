

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def insert_coins():
    print('Please insert coins.')
    num_quarters = int(input('how many quarters?: '))
    num_dimes = int(input('how many dimes?: '))
    num_nickel = int(input('how many nickels?: '))
    num_pennies = int(input('how many pennies?: '))


user_input = input('What would you like? (espresso, latte, cappuccino): ')

insert_coins()

if user_input == 'report':
    print(
        f"water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money}$")

if user_input == 'off':
    print('machine turned off')
    exit()
