#Simple Interest ...

'''print("\nCalculating Simple Interest .....\n")

pr_amount = int(input("Enter the principle amount : "))
no_yr = int(input("Enter the number of years : "))

if no_yr > 12:
     rate_interest = 10
     simple_interest = (pr_amount * rate_interest * no_yr) / 100

else :
    rate_interest = 15
    simple_interest = (pr_amount * rate_interest * no_yr) / 100

print("\n\nPrincipal amount is : ",pr_amount)
print("No of years is : ",no_yr)
print("Rate of interest is : ",rate_interest)
print("Simple Interest is : ",simple_interest)'''


#Simple Interest using function.....
print("\n")
print("Calculating Simple Interest using Function......")
def Input_Pr_Amt():
         pr_amount = int(input("Enter the principle amount : "))
         return pr_amount

def Input_No_Yr():
        no_yr = int(input("Enter the number of years : "))
        return no_yr

def Calc_Interest(no_yr):
        if(no_yr > 12):
             return 10
        else :
             return 15


def Calc_SI(pr_amount,rate_interest,no_yr):
         simple_interest = (pr_amount * rate_interest * no_yr) / 100
         return simple_interest

def Show_Data(pr_amount,no_yr,rate_interest,simple_interest):
        print("\nPrincipal amount is : ",pr_amount)
        print("No of years is : ",no_yr)
        print("Rate of interest is : ",rate_interest)
        print("Simple Interest is : ",simple_interest)

pr_amount = Input_Pr_Amt()
no_yr = Input_No_Yr()
int_rate = Calc_Interest(no_yr)
si = Calc_SI(pr_amount,int_rate,no_yr)
Show_Data(pr_amount,no_yr,int_rate,si)


