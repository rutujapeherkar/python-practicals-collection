print("\nPart 1 :  ")
class Student:
    sname = None
    sroll = None
    def __init__(self):
        self.sname = "Rutuja"
        self.sroll = 22
    def accept(self):
        self.sname = input("Enter Name : ")
        self.sroll = input("Enter Roll NO : ")
    def show(self):
        print("Name is :", self.sname)
        print("Roll No is :", self.sroll)

    def add_instance(self):
        self.savg = input("Enter Average Marks :")

    def __del__(self):
        print("\nDestructor Executed of class Student....")

s1 = Student()
s1.accept()
s1.show()

print("\nExternally adding instances in object 'a1' : ")
s1.sbranch = input("Enter Branch name : ")
print("Branch is :", s1.sbranch)

print("\nInternally adding instance in object 'a1' : ")
s1.add_instance()
print("Average Marks :", s1.savg)

print("\nPart 2 : Class with parameterized contructor")

class Employee:
    eid = None
    ename = None

    def __init__(self, eid, ename ):
        self.eid = eid
        self.ename = ename

    def show_data(self):
        print("Employee ID :", self.eid)
        print("Employee Name :", self.ename)

    def __del__(self):
        print("\nDestructor Executed of class Employee....")

e1 = Employee(101, "Mayur")
e1.show_data()


