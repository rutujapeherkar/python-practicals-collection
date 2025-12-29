print("Question 1")
def check_key_val_present(arg):
    dict1 = {"one": 10, "two": 20, "three": 30, "four": 40, "five": 50, "six": 60}

    for key in dict1.keys():
        if arg == key:
            return True
        for val in dict1.values():
            if arg == val:
                return True
    else:
        return False

a = check_key_val_present(10)
print("10 is present in dictionary :", a)

print("\nQuestion 2")
dict1 = { 'list1': [4, 7, 10, 20],
'list2': [7, 16, 9, 10],
'list3': [13, 10, 4, 8],
'list4': [7, 20, 6, 11]
}

ls2 = []

a = dict1['list1']
print(a)
i = 0

print("\nQuestion 3")
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key = list(dict1.keys())
val = list(dict1.values())
key_sum = 0
val_sum = 0
for i in key:
    key_sum = key_sum + i

for j in val:
    val_sum = val_sum + j

print("Sum of all keys in dictionary is :", key_sum)
print("Sum of all values in dictionary is :",val_sum)


print("\nQuestion 4")
dict1 ={"one": 10, "two":20, "three": 30,"four": 40, "five": 50, "six": 60}
ls = ["three","five"]

print("Initially dict1 is :", dict1)
dict1.pop("three")
dict1.pop("five")
print("Updated dict1 is :", dict1)


print("\nQuestion 5")
ls  = [1, 2, 3, 2, 2, 4, 5, 6, 5, 4, 2, 1, 3, 4, 5, 5, 6, 7, 7, 8, 1, 3, 4, 5, 7, 5]

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0

for ele in ls:
    if ele == 1:
        count1 += 1
    elif ele == 2:
        count2 += 1
    elif ele == 3:
        count3 += 1
    elif ele == 4:
        count4 += 1
    elif  ele == 5:
        count5 += 1
    elif ele == 6:
        count6 += 1
    elif ele == 7:
        count7 += 1
    elif ele == 8:
        count8 += 1

ls2 =[]
ls2.extend([count1,count2,count3,count4,count5,count6,count7,count8])
dict1 = {}
i = 1
j = 0
while i <=8 and j<=7:
    dict1.setdefault(i,ls2[j])
    i = i + 1
    j = j + 1
print("Updated dictionary is :",dict1)

# Question 6: Generate list by repeating keys as per their values
print("Question 6")
dict6 = {1:3, 2:5, 4:5, 7:3, 11:7, 13:2}
ls = []

for k, v in dict6.items():
    ls.extend([k] * v)

print("Generated list:", ls)



# Question 7: Find student with maximum and minimum marks
print("\nQuestion 7")
marks = {"Vinay":61, "Tushar":52, "Vishal":55, "Tanmay":71, "Amey":70, "Amit":65}

max_student = max(marks, key=marks.get)
min_student = min(marks, key=marks.get)

print("Student with maximum marks:", max_student, "→", marks[max_student])
print("Student with minimum marks:", min_student, "→", marks[min_student])



# Question 8: Filter dictionary containing 'in' in key or value
print("\nQuestion 8")
dict8 = {"college": "amazing", "king": "packing", "being": "power", "inning": "donate"}
new_dict = {k: v for k, v in dict8.items() if "in" in k or "in" in v}

print("Filtered dictionary:", new_dict)




















