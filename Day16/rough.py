from turtle import Turtle, Screen
from prettytable import PrettyTable

pt = PrettyTable()
pt.add_column("city_name",["Mumbai", "Delhi", "Kolkata", "Banglore", "Chennai"])
pt.add_column("Person_name", ["Himanshu", "Shail", "Jeewan", "Chaitanya", "Nishant"])

print(pt)


timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()


class car:
    def __init__(self, wheel, steer, body):
        self.wheel = wheel
        self.steer = steer
        self.body = body
        self.followers = 0       # this is a auto updated value

    def __str__(self):
        print(f"My car has {self.wheel}, and {self.steer} with a {self.body} body type")


class new:
    pass

# PascalCasing
# camelCasing
# snake_casing
