

a = 10,20,30
print("Id of a is :", (id(a)))
print("Type of a is :", type(a))

b =[10,20,30]
print("Length of list b is :", (len(b)))

c = ord('A')
print("Ordinal value of 'A' is :", c)

d = chr(32)
print("Character at value 32 is :", d)

e = bin(10)
print('Binary value of 10 is :', e)

f = oct(10)
print("Octal value of 10 is :", f)

g1 = 10
g = hex(g1)
print("Hexadecimal value of 10 is :",g)

h = callable(print)
print(h)

i1 = 10
i = callable(i1)
print(i)

j = isinstance(10,int)
print("Is 10 instance of int ? ",j)

k = isinstance(2.3,object)
print("Is 2.3 instance of object ? ",k)

"""def test():
    pass

l = isinstance(test, function)
print("Is print instance of function ? ",l)"""

m = eval("2 + 3 - 4 * 2 - 0 ")
print("Eval answer is :", m)

n1 = 10
n2 = 9.46
n = eval("n1 + n2")
print(n)

#o =  eval(str(a) + " + " + str(b))
#print(o)

p = min(82,31,24,25,892,145,66)
print(p)

q = min('Abc','Def')
print(q)

r = min('A', 'B')
print(r)

s = max(35,234,30977.56,24884)
print(s)



t1 = 10, 20, 30,4.6
t = sum(t1)
print(t)

u1 = "", 0, 0.0, False
u = any(u1)
print(u)

u2 = "", 0, 0.0, [10]
v = any(u2)
print(v)

w = all([10,5,6,""]) #make parameter tuple or list
print(w)

w1 = all(["Abc", 5, 67.57 ,True])
print(w1)

y =list(range(1,11,1))
print(y)

z = tuple(range(8, 1, -2))
print(z)