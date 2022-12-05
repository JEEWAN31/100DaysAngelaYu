# this lecture is mainly about List and Random Variable
# A list act similar to an array in python
# I have some questions either can we add some elements in a list or not, is at static or Dynamic in nature

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
                     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
                     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee",
                     "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California",
                     "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
                     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)
print(len(states_of_america))
print(states_of_america[3])

fruits = ["Strawberries", "Kale", "Nectarines", "Apples", "Grapes", "Peaches",
          "Cherries", ]

Vegies = ["Pears", "Tomatoes", "Celery", "Potatoes", "Spinach"]

Dirty_Dozen = [fruits, Vegies]

print(Dirty_Dozen[1][1])


#######

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)
