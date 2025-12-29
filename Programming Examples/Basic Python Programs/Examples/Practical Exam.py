#Defining methods
def accept_data():
    print("Enter Principal Amount : ", end = "")
    pr_amt = int(input())
    print("Enter Rate of Interest : ", end = "")
    rate_of_interest = int(input())
    print("Enter Number of Years : ", end = "")
    no_of_years = int(input())
    return pr_amt,rate_of_interest,no_of_years

def calc_simple_interest(pr_amt,rate_of_interest,no_of_years):
    si = (pr_amt*rate_of_interest*no_of_years)/100
    return si

def show_data(pr_amt,rate_of_interest, no_of_years, si):
    print("Principal Amount is :", pr_amt)
    print("Rate of Interest is :", rate_of_interest)
    print("Number of Years :", no_of_years)
    print("Simple Interest :", si)

#Calling methods
pr_amt, rate, year = accept_data()
si = calc_simple_interest(pr_amt,rate, year)

print()
show_data(pr_amt, rate, year, si)