#Q2:
principal_amount = float(input("Enter principal amount P:\n"))
interest_rate = float(input("Interest rate as decimal r:\n"))
interest_per_year = float(input("Enter the number of times the interest is compounded per year n:\n"))
number_of_years = int(input("Number of years t:\n"))

interest = principal_amount*(1 + (interest_rate)/(interest_per_year))**(interest_per_year * number_of_years)
print(round(interest))
