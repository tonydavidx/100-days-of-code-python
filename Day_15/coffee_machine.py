
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

out_of_stock = []


def get_payment():
    print('Please insert coins.')
    total_coins = 0
    num_quarters = 0.25 * int(input('how many quarters?: '))
    num_dimes = 0.10 * int(input('how many dimes?: '))
    num_nickel = 0.5 * int(input('how many nickels?: '))
    num_pennies = 0.1 * int(input('how many pennies?: '))
    total_coins = num_quarters + num_dimes + num_nickel + num_pennies
    return total_coins


def make_coffee(drink):
    drink_cost = MENU[drink]['cost']

    if get_resources(drink) == True:
        print(f'Sorry we are out of {out_of_stock[0]}')
    else:
        print(f"{drink} cost is {drink_cost}")
        payment = get_payment()
        if payment < drink_cost:
            print('Sorry thats not enough money')
        else:
            print(f"Here is your {drink} 🍵. Enjoy!")
            change = payment - drink_cost
            change = format(change, '.2f')
            print(f"Here is your change ${change}")

            global money
            money += drink_cost

            reduce_resources(drink)


def get_resources(drink):
    global out_of_stock
    no_stock = False
    for resource in resources:
        if resource in MENU[drink]['ingredients']:
            if resources[resource] < MENU[drink]['ingredients'][resource]:
                no_stock = True
                out_of_stock.append(resource)
    return no_stock


def reduce_resources(drink):
    global resources

    for resource in resources:
        if resource in MENU[drink]['ingredients']:
            resources[resource] = resources[resource] - \
                MENU[drink]['ingredients'][resource]


while True:
    drinks = ['espresso', 'latte', 'cappuccino']

    user_input = input('What would you like? (espresso, latte, cappuccino): ')

    for d in drinks:
        if d in user_input:
            make_coffee(user_input)

    if user_input == 'report':
        print(
            f"water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: {money}$")

    if user_input == 'off':
        print('machine turned off')
        exit()
