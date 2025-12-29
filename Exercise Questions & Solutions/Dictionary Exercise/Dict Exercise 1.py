print("Question - 1")

ls = [10,  "TWO", 3.4, False , [90,100]]
tup = (226022, "Rutuja", "CO", 90.67, True)

ls.append((110,120))
ls.append(70)
ls.append(80)

def check(seq):
    for i in seq:
        print(type(i))


print("\nList is passed as A.P.")
check(ls)
print("\nTuple is passed as A.P.")
check(tup)

print("\nQuestion - 2\n")

def check2(seq):
    if type(seq) == list:
        tup = tuple(seq)
        return tup
    elif type(seq) == tuple:
        ls = list(seq)
        ls.sort()
        return ls
    elif type(seq) == str:
        s = str(seq)
        return s
    elif type(seq) == bool:
        if seq == True:
            return False
        elif seq == False:
            return True
    else:
        return seq * seq

print("Passing a list as A.P.")
t1 = check2([10,20,30,40,50])
print("Output 1 is :", t1)

print("\nPassing a tuple as A.P.")
t2 = check2((94,53,13,57.3,6.25))
print("Output 2 is :", t2)

print("\nPassing a string as A.P.")
t3 = check2("Rutuja")
print("Output 3 is :", t3)

print("\nPassing a boolean as A.P.")
t4 = check2(True)
print("Output 4 is :", t4)

print("\nPassing an int as A.P.")
t5 = check2(4)
print("Output 5 is :", t5)

print("\nPassing a float as A.P.")
t6 = check2(2.3)
print("Output 6 is :", t6)


print("\nQuestion - 3")
d = {0:10, 1 : 20}
print("Initially d :",d)
d.update({2:30})
print("Updated d :",d)

print("\nQuestion - 4")
dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}

print("Initially dic :",dict1)

dict1.update(dict2)
dict1.update(dict3)
print("Updated dic :",dict1)

print("\nQuestion - 5")
dict1 = {"one" : 10, "two": 20, "three": 30, "four" : 40, "five" : 50, "six" : 60}

for key, value in dict1.items():
    dict1[key] = value
    print(dict1)
    break

print("\nQuestion - 6")
dict1 = {"one" : 10, "two": 20, "three": 30, "four" : 40, "five" : 50, "six" : 60}
'''
i = 1
while dict1.keys():
    val = dict1.keys()
    print(dict[val])
    i = i + 1
'''
print("\nQuestion - 7")
dict1 = {}
ls = []

i = 1
while i <= 10:
    j = 1
    while j<=10:
        mul = i * j
        ls.append(mul)
        j = j + 1
        #dict1[i].update({i:ls})

    i = i + 1
print(dict1)

print("\nQuestion - 8")
dict1 = {1:10, 2:20, 3:30, 4:40, 5:50,6 :60}

dict1[1] = 10 * 10
dict1[2] = 20 * 20
dict1[3] = 30 * 30
dict1[4] = 40 * 40
dict1[5] = 50 * 50
dict1[6] = 60 * 60





