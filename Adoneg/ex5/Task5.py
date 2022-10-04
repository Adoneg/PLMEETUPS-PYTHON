# Q1.
# bonus = 0.05
# year_threshold = 5
# user_salary = int(input("Enter your salary:\n"))
# year_of_service = int(input("Enter your year of service:\n"))
# if year_of_service > 5:
#     net_bonus = bonus * user_salary
#     print(f"Your net bonus is: {net_bonus}frs")


# Q2.
#
# lenght = int(input("Enter the length:\n"))
# breadth = int(input("Enter the breadth:\n"))
#
# if lenght == breadth:
#     print("Square")
# else:
#     print("Not a square")

# Q3

# attendance_threshold = 0.75
# number_of_classes_held = int(input("Enter the number of classes held:\n"))
# number_of_classes = int(input("Enter the number of classes you attended:\n"))
#
# percentage_of_classes_attended = (number_of_classes/number_of_classes_held) * 100
# print(f"percentage of classes attended = {round(percentage_of_classes_attended, 2)}%")
#
# if percentage_of_classes_attended < 0.75:
#     print("You are allowed to enter class")
# else:
#     print("You are not allowed into class")

# # Q4.
# user_age = int(input("Enter your real age😜😜😍:\n"))
# if user_age > 40:
#     if user_age > 60:
#         print("Turning Old")
#     else:
#         print("Middle Age")
# else:
#     print("Young Age")

# Q5
# sample_dict = {0:10, 1:20}
# # sample_dict.update({2:30})
# print(f"Expected Result: {sample_dict}")
# or
# sample_dict = {0:10, 1:20}
# num1 = input("enter num1 or enter 111 to terminate:\n")
# if num1 == 111:
#     breakpoint()
# else:
#     num2 = input("enter num2:\n")
#     sample_dict[num1]=num2
# print(sample_dict)

# using classes to add key and value into  a dict
# class My_dict(dict):
#     def __int__(self):
#         self = dict()
#
#     def add_dict(self, key, value):
#         self[key] = value
#
# dict_object = My_dict()
# dict_object.add_dict(2, 30)
# print(dict_object)

# Q6
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
#
# for (key, value) in dic3.items():
#     dic2.update({key: value})
#     for (key, value) in dic2.items():
#         dic1.update({key: value})
# print(f"Expercted Results:\n {dic1}")
# 0r
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
#
# accumulator = {}
# accumulator.update(dic1)
# accumulator.update(dic2)
# accumulator.update(dic3)
# print(accumulator)

# Q7
# dict = {6: 60, 1: 10, 4: 40, 3: 30,  5: 50, 2: 20}
# key_list = []
#
# for (key, value) in dict.items():
#     key_list.append(key)
# key_list.sort()
# print(key_list)

# Q8
# dict = {6: 60, 1: 10, 4: 40, 3: 30,  5: 50, 2: 20, 7:70, 8:80,
#         9:90, 10:100, 11:110, 12:120, 13:130, 14:140, 15:150, 16: 160,
#         18: 180, 19: 190, 20:200}
#
# for (key, value) in dict.items():
#     print(f"The key is {key} and the value is {value} ")
