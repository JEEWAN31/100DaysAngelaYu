# Procerdural Programming is here to write all of the program which makes the file a lot more hectic and hard top follow all the instruction

# TODO 1. Print report of all the coffes availabale
# TODO 2. Ask user what would they like to take
# TODO 3. turn machine off if they dont want anything from you
# TODO 4. Process Coins
# TODO 5. Check if the transaction is successful
# TODO 6. Update the resources after the transaction is successful

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


def resource_available(x):
    for items in resources:
        if resources[items] < x[items]:
            print(f"Not enough material available for {x}")
            return False
    return True


def report():
    print(f"Water : {resources['water']}")
    print(f"milk : {resources['milk']}")
    print(f"coffee : {resources['coffee']}")


is_coffee = True

while is_coffee:
    coffee = input(f"What would you like to take (latte, espresso, cappuccino")
    if coffee == "Report":
        report()
    if coffee == "OFF":
        is_coffee = False
    else :

