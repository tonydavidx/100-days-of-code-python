from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


machine_on = True
while machine_on:
    choice = input(f'What would you like {menu.get_items()}\n')

    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        machine_on = False

    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            cost = drink.cost
            print(f'{drink.name} cost is {cost}')
            payment = money_machine.make_payment(cost)
            if payment == True:
                coffee_maker.make_coffee(drink)
