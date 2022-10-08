
students_dictionary = {}

not_done = True
while not_done :
    students_name = input("Enter your name or enter 'done' to end.:\n")
    if students_name.lower() == "done":
        break
    students_marks = int(input("Enter mark:\n"))
    students_dictionary.update({students_name : students_marks})
    # students_dictionary[students_name] = students_marks
print(students_dictionary)