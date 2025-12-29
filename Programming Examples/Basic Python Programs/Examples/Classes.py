

class Student:
    def __init__(self,nm,rno,br):
        self.sname = nm
        self.sroll = rno
        self.sbranch = br

    def accept(abc):
        abc.sname = input("Enter student name : ")
        abc.sroll = int(input("Enter student roll no :"))
        abc.sbranch = input("Enter student branch : ")

    def show(self):
        print("Student name is :",self.sname)
        print("Student roll no is :", self.sroll)
        print("Student branch is :", self.sbranch)


s1= Student("",0,"")
print("Accepting details of Student 1 :")
s1.accept()

s2= Student("Shreyas Peherkar",187056,"IT")

print("\nDisplaying Details of Student 1 : ")
s1.show()
print("\nDisplaying Details of Student 2 : ")
s2.show()
