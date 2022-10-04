# Q1.
sentence = "All work and no play makes jack a dull boy"
word_list = sentence.split()
print(word_list)
variable_list = ["var1", "var2", "var3", "var4", "var5", "var6", "var7", "var8", "var9", "var10"]
index = 0
for index in range(len(word_list)):
    variable_list[index] = word_list[index]
    print(f"{variable_list[index]}\n")
    index += 1

# Q2.
print(6*(1-2))

#Q3.
# The output of the code below is -6
print(6*(1-2))
# After commenting no change was recorded in the output.

#Q5.
# def of variable to calculate compount interest
norm_rate_setter = True
if norm_rate_setter:
    annual_norm_rate = 1/100
    norm_rate_setter = False
else:
    annual_norm_rate = -0.05/100

principal_amount =int( input("Please enter principal_amount:\n") )
number_of_years = int(input("enter number of year:\n"))
compounded_interest_per_year = int(input("Enter the value for compounded_interest_per_year:\n"))

compound_interest = (principal_amount)*(1 + (annual_norm_rate/compounded_interest_per_year))**(compounded_interest_per_year)*(number_of_years)
print(f"compound_interest:{compound_interest}")