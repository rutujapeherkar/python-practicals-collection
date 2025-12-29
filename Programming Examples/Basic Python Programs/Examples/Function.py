def Hello():
    print("Hello all")

Hello()

def Test1(a,b,c):
    print(a,b,c)

Test(10,20,30)
Test(a=20,b=10,c=30)

def Test2(*a):
    for var in a:
       print(a)

Test(1,2.23,30)


