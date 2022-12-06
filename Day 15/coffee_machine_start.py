# Procerdural Programming is here to write all of the program which makes the file a lot more hectic and hard top follow all the instruction

# TODO 1. Print report of all the coffees available
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
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
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


def update_ingredients(x):
    for items in x:
        resources[items] -= x[items]
    pass


def process_coins():
    total = 0
    total = total + 10 * int(input("enter the numbers of 10 note \n"))
    total += 20 * int(input("enter the numbers of 20 note \n"))
    total += 50 * int(input("enter the numbers of 50 note \n"))
    total += 100 * int(input("enter the numbers of 100 note \n"))
    return total


is_coffee = True

while is_coffee:
    coffee = input(f"What would you like to take (latte, espresso, cappuccino) \n")
    if coffee == "Report":
        report()
    if coffee == "OFF":
        is_coffee = False
    else:
        x = MENU[coffee]
        if resource_available(x["ingredients"]):
            payments = process_coins()
            if x["cost"] < payments:
                update_ingredients(x["ingredients"])
                print("Your Payment id getting processed \n")
                if payments-x["cost"]>0:
                    print(f"Here is your remaining amount to be refunded : {payments-x['cost']} \n")
                print(f"here is your {} ")


def fill_ingredients():
    resources["water"] += 300
    resources["milk"] += 200
    resources["coffee"] += 100


Yup = input("Whether you would like to fulfill the ingredients again or not")
if Yup == "Yes":
    fill_ingredients()




