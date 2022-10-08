
def add(num1, num2):
    """returns the sum btw two numbers"""
    return num1 + num2

def sub(num1, num2):
    """returns the difference btw two numbers"""
    return num1 - num2
number1 = int(input("Enter the first number:\n"))
number2 = int(input("Enter the second number:\n"))

task = input("Do u want to add or sub🤷, enter add to add or sub to subtract:\n")

if task.lower() == "add":
    sum = add(number1, number2)
    print(sum)
else:
    difference = sub(number1, number2)
    print(difference)
