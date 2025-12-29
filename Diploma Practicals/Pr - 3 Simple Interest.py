print("\nCalculating Simple Interest .....\n")

pr_amount = int(input("Enter the principle amount : "))
no_yr = int(input("Enter the number of years : "))

if no_yr > 12:
     rate_interest = 10
     simple_interest = (pr_amount * rate_interest * no_yr) / 100

else :
    rate_interest = 15
    simple_interest = (pr_amount * rate_interest * no_yr) / 100

print("\nPrincipal amount is : ",pr_amount)
print("No of years is : ",no_yr)
print("Rate of interest is : ",rate_interest)
print("Simple Interest is : ",simple_interest)