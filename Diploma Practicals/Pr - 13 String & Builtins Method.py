str1 = "Computer Department"
str2 = "1234"
print("\n--------- STRING FUNCTIONS ---------")
print(" 1. Capitalized string is :",(str1.capitalize()))
s1 = str1.find("e")
print(" 2. First Occurrence of Letter 'e' is present at location :", s1)
s2 = str1.find('e',9,13)
print(" 3. Occurrence of Letter 'e' from 9 to 13 is present at location :", s2)
print(" 4. Is str1 alphabetic ?? -->", (str1.isalpha()))
print("    Is str2 alphabetic ?? -->", (str2.isalpha()))
print(" 5. Is str1 alphanumeric ?? -->",(str1.isalnum()))
print("    Is str2 alphanumeric ?? -->",(str2.isalnum()))
print(" 6. Is str1 digitic ?? -->", (str1.isdigit()))
print("    Is str2 digitic ?? -->", (str2.isdigit()))
print(" 7. Lowered String 'str1' is -->", (str1.lower()))
print(" 8. Uppered String 'str1' is -->", (str1.upper()))
print(" 9. Is 'str1' is lowercase ?? -->",(str1.islower()))
print("    Is 'str2' is lowercase ?? -->",(str2.islower()))
print(" 10.Is 'str1' is uppercase ?? -->",(str1.isupper()))
print("    Is 'str2' is uppercase ?? -->",(str2.isupper()))
print(" 11.Left Strip 'str1' by 'Comp' -->", (str1.lstrip("Comp")))
print(" 12.Right Strip 'str1' by 'ment' -->", (str1.rstrip("ment")))

print("\n\n--------- BUILTINS FUNCTIONS ---------")
a = 10,20,30
print(" 1. Id of a is :", (id(a)))
print(" 2. Type of a is :", type(a))

b =[10,20,30]
print(" 3. Length of list b is :", (len(b)))

c = ord('A')
print(" 4. Ordinal value of 'A' is :", c)

d = chr(32)
print(" 5. Character at value 32 is :", d)

e = bin(10)
print(' 6. Binary value of 10 is :', e)

f = oct(10)
print(" 7. Octal value of 10 is :", f)

g1 = 10
g = hex(g1)
print(" 8. Hexadecimal value of 10 is :",g)

h = callable(print)
print(" 9. Is print callable ? :",h)

i1 = 10
i = callable(i1)
print("    Is Integer callable ? :",i)

j = isinstance(10,int)
print(" 10.Is 10 instance of int ? :",j)

k = isinstance(2.3,object)
print("    Is 2.3 instance of object ? :",k)

m = eval("2 + 3 - 4 * 2 - 0 ")
print(" 11.Eval answer is :", m)

n1 = 10
n2 = 9.46
n = eval("n1 + n2")
print("    Eval answer is :", n)

p = min(82,31,24,25,892,145,66)
print(" 12.Minimum value is :",p)
r = min('A', 'B')
print("    Minimum value is :",r)

q = max('Abc','Def')
print(" 13.Maximum value is :",q)
s = max(35,234,30977.56,24884)
print("    Maximum value is :",s)


t1 = 10, 20, 30,4.6
t = sum(t1)
print(" 14.Sum is :", t)

'''u1 = "", 0, 0.0, False
u = any(u1)
print(u)

u2 = "", 0, 0.0, [10]
v = any(u2)
print(v)

w = all([10,5,6,""]) #make parameter tuple or list
print(w)

w1 = all(["Abc", 5, 67.57 ,True])
print(w1)'''

y =list(range(1,11,1))
print(" 15.Range answer is :", y)

z = tuple(range(8, 1, -2))
print("    Range answer is :",z)

