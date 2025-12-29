ls = list(range(1,11))
print(" 1. Initially ls :", ls)
ls.append(11)
print(" After append() ls :", ls)

ls2 = list(range(1,6))
print(" 2. Initially ls2 :", ls2)
ls2.extend(["Rutuja", "CO", 90.67, 226022])
print(" After extend() ls2 :", ls2)

ls3 = ["Rutuja", "Shreyas", "Janhvi", "Pavan", "Aransh"]
print(" 3. Initially ls3 :", ls3)
ls3.insert(2,227022)
print(" After insert() ls3 :", ls3)

ls4 = list(range(22,44,2))
print(" 4. Initially ls4 :", ls4)
ls4.clear()
print(" After clear() ls4 :", ls4)

ls5 = [226022, "Rutuja", 226022, "Peherkar", 90.23, False]
print(" 5. Initially ls5 :", ls5)
a = ls5.pop(3)
print(" After pop ls5 :", ls5)
print(" Popped element is :", a)

ls6 = [89,23,256,3,34,13,46]
print(" 6. Initially ls6 :", ls6)
ls6.sort()
print(" Ascending Order :", ls6)
ls6.sort(reverse = True)
print(" Descending Order :", ls6)

ls7 = [1,2,3,1,4,6,89,3,2,4,1,1,2]
print(" 7. Initially ls7 :", ls7)
c = ls7.count(1)
print(" Count of 1 in ls7 :",c)
c = ls7.count(121)
print(" Count of 121 in ls7 :",c)

ls8 = [{1:"Rutuja"}, False, 90,23,"Janhvi", "Abhira", 227044, "CO"]
print(" 8. Initially ls8 :", ls8)
print(" ID of ls8 :", id(ls8))
a = ls8.copy()
print(" After copy() :", a)
print(" ID of new list 'a' :", id(a) )

ls9 = list(range(2,21,2))
print(" 9. Initially ls9 :", ls9)
a = ls9.remove(14)
print(" After remove() of 14 ls9 :", ls9)

ls10 = [10,20,10,30,10,23,134,20,10,90,10]
print(" 10. Initially ls10 :", ls10)
a = ls10.index(10)
print(" After index() ls10 :", ls10)
print(" Index of first occurrence of 10 in ls10 :", a)
b = ls10.index(10,3,8)
print(" Index of occurrence betwen index 3 to 8 of 10 in ls10 :", b)

ls11 = list(range(10,110,10))
print(" 11. Initially ls11 :", ls11)
ls11.reverse()
print(" After reverse() ls11 :", ls11)







