
print("Program 1 : ")
try:
    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter second number : "))
    div = n1/n2
    print("Division is :", div)
except:
    print("Error : Denominator cannot be 0")

print("\nProgram 2 :")

try:
    ls = [2,4,6,0]
    div = ls[5]/ls[3]
    print("Division :", div)
except ZeroDivisionError:
    print("Error : Denominator cannot be 0")
except IndexError:
    print("Error : Index is out of range")

print("\nProgram 3 : Use of finally ...")

try:
    n1 = 10
    n2 = 0
    div = n1/n2
    print("Division is :",div)
except:
    print("Error : Denominator cannot be 0")
finally:
    print("Finally block executed")

print("\nProgram 4: To Raise an Exception")

name = "Rutuja"

if not(type(name)) is int:
    raise TypeError ("Only Integers Are Allowed")