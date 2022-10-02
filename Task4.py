#Even or odd

# user_num = int(input("Enter any number:\n"))
#
# if user_num % 2 == 0:
#     print("I am even")
# else:
#     print("I am odd")

#Length of a word
#
# user_word = input("enter any word:")
#
# lenght_user_word = len(user_word)
# print(lenght_user_word)

#calculate Age
# user_birth_year = int(input("Enter your birth year:\n"))
#
# current_year = int(input("enter your current year:\n"))
#
# user_age = current_year - user_birth_year
# if user_age < 19:
#     print("You are a minor")
# else:
#     print("You are an adult")


#Days to come back
# go_month = 12
# go_day = 13
#
# num_of_weeks = 40
# num_of_months = int(num_of_weeks/4)
#
# for month in range(num_of_months):
#     go_month += 1
#     if go_month == 13:
#         go_month = 1
#
# month_num_dict = {
#     1: "January",
#     2: "February",
#     3: "March",
#     4: "April",
#     5: "May",
#     6: "June",
#     7: "July",
#     8: "August",
#     9: "September",
#     10: "October",
#     11: "November",
#     12: "December"
# }
# print(f"You will  come back on {go_day}th of {month_num_dict[go_month]}")

#name_sex dictionary

# number_of_expected_students = 3
# student_name_list = []
# student_sex_list = []
# student_name_sex_dict = {}
# while number_of_expected_students > 0:
#     students_name = input("enter your name:\n")
#     student_name_list.append(students_name)
#     students_sex = input("enter your sex:\n")
#     student_sex_list.append(students_sex)
#
#     #dict comprehension
#     # dict = {item: item_value for item in list}
#     student_name_sex_dict = {name: student_sex_list[student_name_list.index(name)] for name in student_name_list}
#     number_of_expected_students -= 1
# first_five_items = list(student_name_sex_dict.items())[0:5]
# print(first_five_items)

# d = {'s': 1, "d": 4, "l":2, "t":3, "u":12}
# print(list(d.items())[:2])

# print the first n_items from a dict
# def take(n, iterable):
#     """Return first n items of the iterable as a list"""
#     return list(islice(iterable, n))
#
# n_items = take(n, d.iteritems())
