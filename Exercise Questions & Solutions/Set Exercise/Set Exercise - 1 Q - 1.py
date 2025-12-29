
set = {10,20,"ABC", False, 90.67}
print("a. To iterate")
for ele in set :
    print(ele)

#b. to add members
print("\nInitially : ",set)
set.add(30)
print("Updated : ",set)

#c. To remove items using discard
print("\nInitially : ",set)
set.discard(90)
print("Updated : ",set)

#d. remove using remove
print("\nInitially : ",set)
set.remove(10)
print("Updated : ",set)

#e .to print length of set elements
count = len(set)
print("\nCount of elements in a set is :  ",count)

#f. smallest and largest ele from set

set2 = {10,20,30, 40.45, 65}
ls = list(set2)

i = 0
great = 0
small = 100
while i < len(ls):
    if ls[i] > great :
        great = ls[i]
    elif ls[i] < small :
        small = ls[i]
    i = i +1

print("\nElements in 'set2' is : ",set2)
print("Smallest element in the set is : ", small)
print("Largest element in the set is : ", great)

set2 = {10,20,30, 40.45, 65}

for a in set2:
    if a>great:
        great = a
    if a<small:
        small = a

print("Smallest element in the set is : ", small)
print("Largest element in the set is : ", great)

#g. Remove all elements

set3 = {10,20,30,40,50}
print("\nInitially 'set3' is : ", set3)
set3.clear()
print("Updated 'set3' is : ",set3)

#h. to check presence

set4 = {10,20,30,40,23}
ls2 = list(set4)
num = int(input("enter no"))

i = 0
while i<len(set4):
    temp = set4.pop()
    if num == temp:
        print("Elemenmt presemt")
        break
    i = i + 1


print(num)
i = 0
while i<len(set4):
    temp = set4.pop()
    if num>temp:
        great = num
    if num<temp:
        small = num
    i = i + 1

print(great)
print(small)















