
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
    total_coins = 0
    # num_quarters = 0.25 * int(input('how many quarters?: '))
    # num_dimes = 0.10 * int(input('how many dimes?: '))
    # num_nickel = 0.5 * int(input('how many nickels?: '))
    # num_pennies = 0.1 * int(input('how many pennies?: '))
    # total_coins = num_quarters + num_dimes + num_nickel + num_pennies
    total_coins = 11.5
    return total_coins


def get_drink(drink):
    drink_cost = MENU[drink]['cost']
    print(f"{drink} cost is {drink_cost}")
    user_money = insert_coins()

    if user_money < drink_cost:
        print('Sorry thats not enough money')
    else:
        print(f"Here is your {drink} 🍵. Enjoy!")
        change = user_money - drink_cost
        print(f"Here is your change ${change}")

    global money
    money += drink_cost


while True:
    drinks = ['espresso', 'latte', 'cappuccino']

    user_input = input('What would you like? (espresso, latte, cappuccino): ')

    for d in drinks:
        if d in user_input:
            get_drink(user_input)

    if user_input == 'report':
        print(
            f"water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money}$")

    if user_input == 'off':
        print('machine turned off')
        exit()
