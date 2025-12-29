print("\nQuestion - 1")

set1 = {10,20,30,40}
set2 = {20,40,50}
print("Initially set1 : ",set1)
print("Initially set2 : ",set2)
set1.difference_update(set2)
print("Updated set1 : ",set1)
print("Updated set2 : ",set2)

print("\nQuestion - 2")
set1 = {10,20,30,40,50}
print("Initially set1 : ",set1)
set1.remove(10)
set1.remove(20)
set1.remove(30)
print("Updated set1 : ",set1)

print("\nQuestion - 3")
set1 = {10,20,30,40,50}
set2 = {60,70,80,90,10}
print("Initially set1 : ",set1)
print("Initially set2 : ",set2)
set3 = set1.intersection(set2)
print("Updated set1 : ",set1)
print("Updated set2 : ",set2)
print("Common elements are : ", set3)

print("\nQuestion - 4")
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
print("Initially set1 : ",set1)
print("Initially set2 : ",set2)
set1.symmetric_difference_update(set2)
print("Updated set1 : ",set1)
print("Updated set2 : ",set2)

print("\nQuestion - 5")
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
print("Initially set1 : ",set1)
print("Initially set2 : ",set2)
set1.intersection_update(set2)
print("Updated set1 : ",set1)
print("Updated set2 : ",set2)

print("\nQuestion - 6")
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
print("Initially set1 : ",set1)
print("Initially set2 : ",set2)
set3 = set1.intersection(set2)
print("Updated set1 : ",set1)
print("Updated set2 : ",set2)
print("Updated set3 : ",set3)

print("\nQuestion - 7")
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
print("Initially set1 : ",set1)
print("Initially set2 : ",set2)
set3 = set1.union(set2)
print("Updated set1 : ",set1)
print("Updated set2 : ",set2)
print("Updated set3 : ",set3)















