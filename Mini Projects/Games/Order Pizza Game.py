a = input("Enter the size of pizza you want (S/M/L) : ")
b = input("Do you want Pepperoni pizza ? (Y/N) : ")
bill= 0
if a == 'S' or a =='s':
   bill = 100
elif a == 'M' or a == 'm':
   bill = 200
elif a == 'L' or a == 'l':
   bill = 300

if b == 'Y' or b == 'y':
   c = input("Do you want to add extra cheese (Y/N) : ")
   if a == 's' or a == 'S':
      bill = bill + 50
      if c == 'y' or c== 'Y':
          bill = bill + 50

   elif a == 'm' or a == 'M':
      bill = bill +100
      if c == 'y' or c== 'Y':
          bill = bill + 50

   elif a == 'l' or a == 'L':
      bill = bill + 150
      if c == 'y' or c== 'Y':
          bill = bill + 50

print("Your total bill is :",bill)
