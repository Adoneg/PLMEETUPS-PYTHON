# Q2.
# current_time = 2
# num_of_hours = 51
# pm_or_am = "pm"
#
# for _ in range(num_of_hours):
#     current_time += 1
#     if current_time == 13:
#         current_time = 1
#         pm_or_am = "am"
# print(f"Alarm goes off at {current_time}{pm_or_am}")

# Q3.
current_time = int( input("Enter the current time:\n") )
num_of_hours = input("Enter the number of hours:\n")
pm_or_am = "pm"

for _ in range(int(num_of_hours)):
    current_time += 1
    if current_time == 13:
        current_time = 1
        pm_or_am = "am"
print(f"Alarm goes off at {current_time}{pm_or_am}")

# Q4.

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(list[-8:-3])

# Q5.
# name = "John"
# time = "centuries"
# years = 333
#
# print(f"Money had ruled over the world for 9 {time} and it cause so much damage to the life  of {name}"
#       f" that he had to leave earth for {years} years")