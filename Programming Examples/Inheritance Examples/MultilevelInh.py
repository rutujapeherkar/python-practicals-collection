class A:
    def __int__(self, roll, name):
        self.roll = roll
        self.name = name

    def show(self):
        print("Roll number : ", self.roll)
        print("Name : ",self.name)

class B(A):
    def __int__(self,roll, name, m1,m2,m3,m4,m5):
        A.__init__(roll, name)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
        self.tot = 0

    def calc(self):
        self.tot = self.m1 + self.m2 + self.m3 + self.m4 + self.m5

    def show(self):
        super().show()
        print("Total marks : ", self.tot)


class C(B):
    def __init__(self,roll, name,m1,m2,m3,m4,m5,grade):
        B.__init__(roll,name,m1,m2,m3,m4,m5)
        self.grade = grade

    def show(self):
        super().show()
        print("Grade of student is : ", self.grade)

c1 = C(226022,"Rutuja", 96,89,89,77,97,"A")
c1.calc()
c1.show()