# # List Comprehension here the iterable can be a range, list , string or
# import random
#
# numbers = [1, 2, 3, 4]
# ans= []
# for num in numbers:
#     add = num+1
#     ans.append(add)
#
# # This is a list comprehension
# new_list = [num+1 for num in numbers]
# # new_list = [new_item for item in list ]
#
# # conditional List comprehension
name = ["Jeevan", "Sumit", "Raj", "Mohit", "shail", "Shitty"]
# # new_list = [item for item in list if case]
# short_name = [x.upper() for x in name if len(x)>5]
# print(short_name)
#
# with open('file1.txt') as file1:
#     list1 = file1.readlines()
#
# with open('file2.txt') as file2:
#     list2 = file2.readlines()
#
# final_list = [int(num) for num in list1 if num in list2]
# print(final_list)
#
#
# # Dictionary Comprehension : Create new dictionary forma  given list or a dictionary
#
# # new_dict = {new_key: new_value for item in list}
# # new_dict = {new_key : new_value for (key,value) in dict.items()}
# # new_dict = {new_key : new_value for (key,value) in dict.items() if condition}
import random

score = {item: random.randint(80, 100) for item in name}
print(score)

topper = {student: score for (student, score) in score.items() if score > 90}
print(topper)