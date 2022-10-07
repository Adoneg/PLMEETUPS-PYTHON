

#Q4
# NameError: bruce + 4

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