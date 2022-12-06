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


class car:
    def __init__(self, wheel, steer, body):
        self.wheel = wheel
        self.steer = steer
        self.body = body

    def __str__(self):
        print(f"My car has {self.wheel}, and {self.steer} with a {self.body} body type")


class new:
    pass

# PascalCaseing
# camelCasing
# sanke_casing
