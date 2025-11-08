principal_amount = int(input("enter principal amount: "))

number_of_years = int(input("enter number of years: "))

rate_of_interest = float(input("enter rate of interest: "))

interest_amount = (principal_amount * number_of_years * rate_of_interest/100)
total_amount = principal_amount + interest_amount

print("interest_amount", interest_amount)
print("total_amount", total_amount)