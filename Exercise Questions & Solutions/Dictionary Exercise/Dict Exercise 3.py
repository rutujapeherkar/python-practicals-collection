
print("Question - 1")
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
d = {}

j = 0
for i in keys:
     d.update({i:values[j]})
     j = j + 1

print("Updated d is :", d)

print("\nQuestion - 2")
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

print("Initial dict1 is :", dict1)

for i in dict2.keys():
    dict1.setdefault(i)
    dict1[i] = dict2.get(i)
print("Updated dict1 is :", dict1)

print("\nQuestion - 3")
sampleDict = {
 "class": {
 "student": {
 "name": "Mike",
 "marks": {
 "physics": 70,
 "history": 80
 }
}
 }
}

print(sampleDict["class"]["student"]["marks"]["history"])


print("\nQuestion - 4")
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dict = {}

for i in employees:
    dict.setdefault(i,defaults)

print("Dictionary is :",dict)

print("\nQuestion - 5")
sample_dict = {
 "name": "Kelly",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

#Keys to extract
#keys = ["name", "salary"]

ndic = {}
k1 = sample_dict.keys()

for k in k1:
    if k == "name":
        ndic.setdefault(k,sample_dict[k])
    elif k  == "salary":
        ndic.setdefault(k, sample_dict[k])

print("New Dictionary is :",ndic)

print("\nQuestion - 6")
sample_dict = {
 "name": "Kelly",
 "age": 25,
 "salary": 8000,
 "city": "New york"
}

print("Initially is :", sample_dict)
sample_dict.pop("name")
sample_dict.pop("salary")

print("Updated is :", sample_dict)

print("\nQuestion - 7")
sample_dict = {'a': 100, 'b': 200, 'c': 300}
j = 0
for i in sample_dict.values():
    if i == 200:
        print('200 present in a dict')
        break

print("\nQuestion - 8")
sample_dict = {
 "name": "Kelly",
 "age":25,
 "salary": 8000,
 "city": "New york"
}
print("Initially is :", sample_dict)

sample_dict.pop("city")
sample_dict.setdefault("location","New York")

print("Updated is :", sample_dict)

































