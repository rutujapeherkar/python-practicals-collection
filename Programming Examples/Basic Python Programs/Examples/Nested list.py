print("Logic : 1")
ls = []
num = 1
i = 0
while i<=2:
    ls.append([])
    j = 1
    while j<=3:
        ls[i].append(num)
        j = j + 1
        num = num + 1
    i = i +1
print(ls)

print("\nLogic : 2")
ls1 = []
ls2 = [1,2,3]
ls3 = [4,5,6]
ls4 = [7,8,9]
ls1.append(ls2)
ls1.append(ls3)
ls1.append(ls4)
print(ls1)
