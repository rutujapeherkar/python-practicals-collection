#Python Ex-1 : Reverse given list

aList = [100,200,300,400,500]
print("Initial list is : ", aList)
aList.reverse()
print("Reversed list is : ", aList)

aList1 =  [100,200,300,400,500]
a = len(aList1)
aList2 = [0,0,0,0,0]
i = 0
j = 4
while i<a and j<a:
    aList2[i] = aList1[j]
    i = i+1
    j = j-1

print("Reversed list is : ", aList2)

#Python Ex - 1 : Exercise 2: Given a Python list, find value 20 in the list, and if it is present,
# replace it with 200. (Only update the first occurrence of a value.)

list1 = [5,10,15,20,25,50,20]
print("\nInitial list is : ", list1)
a = list1.index(20)
list1[a] = 200
print("Find 20 and replace with 200 :",list1)

list2 = [5,10,15,20,25,50,20]
print("Initial list is : ", list2)
i = 0
while i<7:
    if list2[i] == 20:
        list2[i] = 200
        break
    i = i + 1
print("Find 20 and replace with 200 :",list2)

#Python Exercise 3: Concatenate two lists index-wise.

list1 = ["M","na","i","Ke"]
list2 = ["y", "me", "s", "lly"]

print("\nInitial list is : ", list1)
print("Initial list is : ", list2)
list1.insert(1, list2[0])
list1.insert(3,list2[1])
list1.insert(5,list2[2])
list1.insert(7,list2[3])
print("Updated list after concatenation is : ", list1)

ls1 = ["M","na","i","Ke"]
ls2 = ["y", "me", "s", "lly"]
print("Initial list is : ", ls1)
print("Initial list is : ", ls2)

ls3 = ls1
i = 0
while i<4:
    s1 = ls1[i]
    s2 = ls2[i]
    ls3[i] = s1 + s2
    i = i + 1
print("Updated list after concatenation is : ", ls3)

#Exercise 4: Given a Python list of numbers. Turn every item of a list into its square

aList = [1, 2, 3, 4, 5, 6, 7]
print("\nInitial list is : ", aList)
i = 0
while i<6:
    aList[i] = aList[i] * aList[i]
    i = i + 1
print("Updated list with square's :", aList)

#Exercise 5: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 =[]
print("Initial list is : ", list1)
print("Initial list is : ", list2)

list3 = list1 + list2
print("Updated list after concatenation is : ", list3)

#Exercise 6: Given a two Python list. Iterate both lists simultaneously such that list1 should
# display item in original order and list2 in reverse order.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

i =0
j = 3
while i<4 and j>=0:
    print(list1[i] , end = "  ")
    print(list2[j])
    i =  i +1
    j =  j - 1









