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