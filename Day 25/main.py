# with open ("weather_data.csv") as filename:
#     data = filename.readlines()
#     print(data)

import csv

import pandas
import pandas as pd

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#         print(row)
#     print(temperature)

data = pd.read_csv("weather_data.csv")
print(type(data["temp"]))
# DataFrame and Series : equivalent to a list in a pyhton
f = data.to_dict()
print(f)
data_list = data["temp"].to_list()
# sum = 0
# for num in data_list:
#     sum += num
# print(f"The average temperature of the table is {sum/len(data_list)}")
print(f"The Average temperature of the table is {sum(data_list)/len(data_list)}")
print(data["temp"].mean())

print(data.day)
print(data["day"])
print(data[data.temp == data.temp.max()])

###############################
data_dictionary = {
    "student": ["Amy", "Jeewan", "Ram"],
    "Section": ["A", "B", "C"]
}

data = pandas.DataFrame(data_dictionary)
data.to_csv("new_data.csv")
print("Holly Shitt")

print(len(data_list))

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")







