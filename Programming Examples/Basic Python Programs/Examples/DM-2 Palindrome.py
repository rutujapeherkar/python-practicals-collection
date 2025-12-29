#To check whether entered number is palindrome number or not

print("Enter any 3 digit number : ")
num = int(input())

temp = num

r1 = num % 10
num = num//10
r2 =  num % 10
num=  num//10

num1 = r1 * 100 + r2 * 10 + num

if(num1 == temp):
    print("Entered number ", temp, " is a palindrome number")

else:
    print("Entered number ", temp, " is not a palindrome number")

