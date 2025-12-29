class A:
    def __init__(self,roll,name):
        self.roll = roll
        self.name = name

    def show(self):
        print("Roll No :",self.roll)
        print("Name :",self.name)

class B(A):
    def __init__(self,roll,name,percentage):
        A.__init__(roll,name)
        self.percentage = percentage

    def show(self):
        super().show()
        print("Percentage : ",str(self.percentage))

class C(A):
    def __init__(self,roll,name,sp_grade):
        A.__init__(roll,name)
        self.sp_grade = sp_grade

    def show(self):
        super().show()
        print("Sport's grade : ",self.sp_grade)

print("Object of DC 'B' : ")
b = B(226022,"Rutuja",90.67)

print("\nObject of DC 'C' : ")
c = C(227044,"Pavan","A")

print("\nShowing details of object 'b' : ")
b.show()

print("\nShowing details of object 'c' : ")
c.show()


