interest_rate = float(input("Enter the interest rate: "))
principal = int(input("Enter the principal: "))
n_payments_per_year = int(input("Enter the n payments per year: "))
n_years = int(input("Enter the number of years: ")) 
upper = interest_rate * (principal/n_payments_per_year)
lower = ((interest_rate/n_payments_per_year)+ 1)
exp = -(n_payments_per_year * n_years)
final = 1-(lower)**exp
print(final)
pay = upper/lower
print(pay)
