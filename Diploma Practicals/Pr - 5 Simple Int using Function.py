def accept_data():
    pr_amt = int(input("Enter Principal Amount : "))
    no_of_years = int(input("Enter Number of years : "))
    return pr_amt,no_of_years

def calc_rate_of_interest(no_of_years):
    if no_of_years > 12:
        rate_interest = 10
    else:
        rate_interest = 15
    return rate_interest

def calc_simple_int(pr_amt,rate_of_interest,no_of_years):
    simple_interest = (pr_amt * rate_of_interest * no_of_years) / 100
    return simple_interest

pr_amt, no_of_years = accept_data()
rate_of_interest = calc_rate_of_interest(no_of_years)
simple_interest = calc_simple_int(pr_amt, rate_of_interest,no_of_years)

print("\nPrincipal Amount is :", pr_amt)
print("Rate of Interest is :", rate_of_interest)
print("No of years is :",no_of_years)
print("Simple Interest = ",simple_interest)