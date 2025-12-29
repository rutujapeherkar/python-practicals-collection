num = float(input("Enter a 4 digit number to reverse it : "))

n1 = num%10
num = num//10
n2 = num%10
num = num//10
n3 = num%10
num = num//10
rev = int((n1 *1000) + (n2*100) + (n3*10) + num)
print("Reversed 4 digit Number is :",rev )