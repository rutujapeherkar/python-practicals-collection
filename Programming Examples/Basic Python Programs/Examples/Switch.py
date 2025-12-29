
n1 = int(input("Enter 2 values : "))
n2 = int(input())

while(1):

    print("\n***** Arithematic Operations are ***** ")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Float Division")
    print("5.Float Division")
    print("6.Modulus")
    print("7.Exit ")

    ochoice = int(input("\nSelect the operation you want to perform : "))

    def add(a,b):
        return a + b
    def sub(a,b):
        return a - b
    def mult(a,b):
        return a * b
    def div(a,b):
        return a/b
    def quotient(a,b):
        return a//b
    def remainder(a,b):
        return a % b

    if(ochoice==1):
        add = add(n1,n2)
        print("Addition of ",n1, " + ",n2, " is : ",add)

    elif(ochoice==2):
        sub = sub(n1, n2)
        print("Subtraction of ", n1, " - ", n2, " is : ", sub)

    elif(ochoice == 3):
        mult = mult(n1, n2)
        print("Multiplication of ", n1, " * ", n2, " is : ", mult)

    elif(ochoice== 4):
        div = div(n1, n2)
        print("Float division of ",n1 , " / ", n2, " is : ",div)

    elif(ochoice == 5):
        quotient = quotient(n1,n2)
        print("Floor division of ",n1 , " // ", n2, " is : ",quotient)

    elif(ochoice == 6):
        remainder = remainder(n1,n2)
        print("Remainder of " , n1, " % ", n2, " is : ",remainder)

    elif(ochoice == 7):
        print("\nExited succesfully...")
        break

    else:
        print("\nYou have entered wrong choice ...")

    print("\nDo you want to continue the operation : ( Y / N ) ")
    uchoice = input()

    if(uchoice == 'N' or uchoice == 'n'):
        
        break

    else:
        print("\nAgain performing the operation...")






