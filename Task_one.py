 # Q1. create a dict with keys being the names of students and values or locks
 # being their class number and print out the first student and his/her class number

class_dict = {
     'miriam': 1,
     'shammah': 2,
     'uyaka': 3,
     'Emma': 4
    }
names_of_students = []
for key, value in class_dict.items():
    names_of_students.append(key)

first_student = names_of_students[0]
first_student_class_num = class_dict['miriam']

print(f'first_student:{first_student}\n class number:{first_student_class_num}')

# Q2. Create two intergers containing any numbers and add them and print the result

num1 = 3
num2 = 4
sum = num1 + num2
print(f'sum={sum}')

# Q3. create a list containing 1 interger, 1 string, 1 float and  1 boolean

list = [1, "Adoneg", 12.45, True]
