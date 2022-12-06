# TODO 1. Write the whole code by yourself
# Importing classes from other files
from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

menu = Menu()
# menuItem = MenuItem()
moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()

is_on = True
total_profit = 0

while is_on:
    item = input(f"What would you like to take (cappuccino , latte, espresso: \n )")
    if item == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif item == "OFF":
        is_on = False
    else:
        x = menu.find_drink(item)
        if moneyMachine.make_payment(x.cost) and coffeeMaker.is_resource_sufficient(x):
            coffeeMaker.make_coffee()



