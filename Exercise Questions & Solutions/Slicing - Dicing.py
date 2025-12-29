
print("\n******** Examples of SLICING *******\n")
str1 = "RutujaPeherkar"
a1 = str1[0:8]
print(a1)
a2 = str1[:9]
print(a2)
a3 = str1[:]
print(a3)
a4 = str1[4:8]
print(a4)
a5 = str1[:8]
print(a5)
a6 = str1[3:]
print(a6)
a7 = str1[3:7]
print(a7)

ls = [10,"Abc",90.67, 226022, "RBP","Rutuja",300]
a8 = ls[:]
print(a8)

tup = (10,20,30,40,50,60)
a9 = tup[4:6]
print(a9)
a10 =tup[:8]
print(a10)

str2 = "Python Programming"
a11 = str2[0:8]
print(a11)
a12 = str2[:]
print(a12)
a13 = str2[0:]
print(a13)
a14 = str2[5:]
print(a14)
a15 = str2[:4]
print(a15)

print("\n******** Examples of DICING *******\n")
str3 = "Rutuja Peherkar"
b1 = str3[::-2]
print(b1)
b2 = str3[8::-2]
print(b2)
b3 = str3[::-1]
print(b3)
b4 = str3[10:2:-3]
print(b4)
b5 = str3[:2:-3]
print(b5)
b6 = str3[-1:9:-2]
print(b6)

list = [1,2,3,4,5]
b7 = list[::-1]
print(b7)
b8 = list[1::-3]
print(b8)
b9 = list[:5:-2]
print(b9)

tuple = (10,20,30,40,50,60)
b10 = tuple[::-4]
print(b10)
b11 = tuple[-3::-1]
print(b11)
b12 = tuple[::-1]
print(b12)
b13 = tuple[::]
print(b13)
b14 = tuple[-1:4:-3]
print(b14)
b15 = tuple[1:4:-2]
print(b15)







