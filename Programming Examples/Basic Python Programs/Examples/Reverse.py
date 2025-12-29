num = int(input("Enter any 3 digit number : "))

print("Original Number is ", num)
def reverse(num):
    r1 = num % 10
    #print(r1)
    num = num // 10
    r2 =num % 10
    #print(r2)
    num = num //10;
    r3 = num % 10
    #print(r3)
    s = (r1 * 100) + (r2 * 10) + (r3 * 1)
    return s


r = reverse(num)
print("Original Number is ", num)

print("Reverse number is ",r)


