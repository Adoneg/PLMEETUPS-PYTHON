 # Q1. create a dict with keys being the names of students and values or locks
 # being their class number and print out the first student and his/her class number

class_dict = {
     'Miriam': 1,
     'Shammah': 2,
     'Uyaka': 3,
     'Emma': 4
    }
names_of_students = []
for key, value in class_dict.items():
    names_of_students.append(key)

first_student = names_of_students[0]
first_student_class_num = class_dict['Miriam']

print(f'first_student:{first_student}\n class number:{first_student_class_num}')
