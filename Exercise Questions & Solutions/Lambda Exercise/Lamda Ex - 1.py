from functools import reduce

print("Question 1")
add = lambda n: n + 15

a1 = add(10)
print(a1)

print("\nQuestion 2")
ls = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

print("\nQuestion 3")
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

get_even = lambda n: n%2 == 0
get_odd = lambda n: n%2 != 0

a1 = list(filter(get_even,ls))
a2 = list(filter(get_odd, ls))
print(a1)
print(a2)

print("\nQuestion 4")
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

get_sq = lambda n : n*n
get_cube = lambda n : n*n*n

a1 = list(map(get_sq,ls))
a2 = list(map(get_cube,ls))

print(ls)
print(a1)
print(a2)

print("\nQuestion 5")
date = "2020-01-15"
get_d = lambda n: n!="-"

a = tuple(filter(get_d,date))
print(date)
s1 = str(a[0]+ a[1]+a[2] +a[3])
s2 = str( a[5])
s3 = str(a[6] + a[7])
print(s1)
print(s2)
print(s3)

print("\nQuestion 6")
n1 = 0
get_fib = lambda n : n1+n

ls = list(range(1,6))
a1 = list(map(get_fib,ls))
print(a1)

print("\nQuestion 8")
ls = [1, 2, 3, 5, 7, 8, 9, 10]

c_even = lambda n : True if n % 2 == 0 else False
c_odd = lambda n : True if n %2 != 0 else False
a1 = list(filter(c_even,ls))
a2 = list(filter(c_odd, ls))
l1 = len(a1)
l2 = len(a2)
print("Even count is :",l1)
print("Odd count is :", l2)

print("\nQuestion 9")
ls = [-1, 2, -3, 5, 7, 8, 9, -10]
ls.sort()
ls[:]
print(ls)
rev1 = lambda n: True if n>0 else False
rev2 = lambda n: True if n<0 else False
a1 = list(filter(rev1,ls))
a2 = list(filter(rev2,ls))
a1.extend(a2)
print(a1)

print("\nQuestion 10")
ls = ['ABHAY', 'AMIT', 'MONDAY', 'THURSDAY', 'SAM', 'VISHWAMBHAR', 'JOSHI', 'KULDEEP']
name6 = lambda nm: True if len(nm) >=6 else False
a1 = list(filter(name6,ls))
print(a1)

print("\nQuestion 11")
ls1 = [1, 2, 3]
ls2 = [4, 5, 6]

add = lambda n1,n2 :n1 + n2
a1 = list(map(add,ls1,ls2))
print(a1)

print("\nQuestion 12")
ls = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
divisible = lambda n : True if n/13 or n/19 else False
a1 = list(filter(divisible,ls))
print(a1)

