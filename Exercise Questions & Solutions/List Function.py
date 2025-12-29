
ls = [10,20,"ABC",True, 96.90]
print("Initial list 'ls' is :",ls)
ls.append(50)
print("Updated list 'ls' after append() is :",ls)

ls.extend((60,70,80))   #compulsory requires a sequence as parameter
print("Initial list 'ls' is :",ls)
print("Updated list 'ls' after extend() is :", ls)
ls.extend({1 : "Rutuja", 2: "Peherkar"})
print("Updated list 'ls' after extend() is :", ls)

ls1 = ls.copy
print("Afer using copy() : ")
print("ID of ls is : ", id(ls))
print("ID of ls1 is : ", id(ls1))

ls.reverse()
print("Initial list 'ls' is :",ls)
print("Updated list 'ls' after reverse() is : ", ls)

ls2 = [1,2,3,4,5,6]
ls2.clear()
print("Initial list 'ls2' is :",ls2)
print("Updated list 'ls2'after clear() is :", ls2)

ls.remove(10)
print("Initial list 'ls' is :",ls)
print("Upadated list 'ls' after remove() is:",ls)

ls3 = [226022, "Rutuja ", "CO", "Second year", 226022]
print("Initial list 'ls3' is :",ls3)
ls3.pop(1)
print("Updated list 'ls3' after pop() is : ", ls3)
ls3.pop()
print("Updated list 'ls3' after pop() is : ", ls3) #if ind. not specified then it pops -1

a = ls.count(True)    #Returns the count of non-zero values
print("Initial list 'ls' is :",ls)
print("Count of 'True' in 'ls' is :",a)

ls4 = [10,20,30,40,10,20,20,True]
b = ls4.index(10)
print("Initial list 'ls4' is :", ls4)
print("Index of first occ. of  10 in 'ls4' is:",b)
c = ls4.index(10,3,6)
print("Index of 10 in 'ls4' is:",c)
d = ls4.index(True)
print("Index of True in 'ls4' is:",d)

ls5 = list([ "Shreyas", "Rutuja", "Papa", "Dada","ABC", "CO", "IT"])
print("Initial list 'ls5' is :", ls5)
ls5.sort()
print("Updated list 'ls5' after sort in Asc. order is :", ls5)
ls5.sort(reverse=True)
print("Updated list 'ls5' after sort in Asc. order is :", ls5)

print("Initial list 'ls5' is :", ls5)
ls5.insert(2,"Peherkar")
print("Updated list 'ls5' after insert() at 2nd index is :", ls5)







