import random

n = int(input("\nEnter the number of players : "))
ls = []
print("Initial list is : ", ls)

i = 0
while i<n:
    ls.append([])
    i = i + 1

print("Updated list is : ",ls)

j = 1
while j<=n:

        i = 0
        while i <n:
            roll= random.randint(1,6)
            ls[i].append(roll)
            i = i +1

        print("\n-------------------- ROUND",j," -------------------- ")
        print(ls)
        j = j + 1




