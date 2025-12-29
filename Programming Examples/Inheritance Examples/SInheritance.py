

class Student:
    sname = ""
    sroll = 0
    sbranch = ""

    def __init__(self, nm, roll, br):
        self.sname = nm
        self.sroll = roll
        self.sbranch = br

    def accept(self):
        self.sname = input("Enter student name : ")
        self.sroll = int(input("Enter student roll no :"))
        self.sbranch = input("Enter student branch : ")

    def show(self):
        print("Student name is :", self.sname)
        print("Student roll no is :", self.sroll)
        print("Student branch is :", self.sbranch)

class Marks(Student):
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    avg = 0.0

    def __init__(self,nm,roll,br,m1,m2,m3,m4,m5):
        super().__init__(nm,roll,br)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
        self.avg = 0

    def accept(self):
        super().accept()
        print("Enter marks of 5 subject's : ")
        self.m1 = int(input())
        self.m2 = int(input())
        self.m3 = int(input())
        self.m4 = int(input())
        self.m5 = int(input())

    def calc(self):
        self.avg = self.m1 + self.m2 + self.m3 + self.m5

    def show(self):
        super().show()
        print("Average is :",self.avg,"/500")


print("Accepting Details of a student 1 : ")
m1 = Marks("", 0, 0.0, 0,0,0,0,0,)
m1.accept()
m1.calc()
print("Showing Details of a student 1 : ")
m1.show()

print("Accepting Details of a student 2 : ")
m2 = Marks("", 0, 0.0, 0,0,0,0,0,)
m2.accept()
m2.calc()
print("\nShowing Details of a student 2:")
m2.show()