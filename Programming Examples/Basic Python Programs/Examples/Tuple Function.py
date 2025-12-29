
tup = tuple((10,20,"ABCD",False, 10,True ,90.78))
a = tup.count(10)
print("Count of 10 in tuple is :",a)
b = tup.count(True)
print("Count of True in tuple is :", b)

tup1 = (226022, "Rutuja", 90.67, True, "CO",226022)
a = tup1.index("Rutuja")
print("Element 'Rutuja' is present at index :",a)
b = tup1.index(226022)
print("Element '226022' first occured at index :",b)
c = tup1.index(226022,2,6)
print("Element '226022' is present at index :",c)

