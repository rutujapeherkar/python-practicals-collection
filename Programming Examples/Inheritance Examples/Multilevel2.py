class A:
    def m1(self):
        print("Hello from m1() of Base class 'A' ")

class B(A):
    def m2(self):
        super().m1()
        print("Hello from m2() of Intermediate class 'B' ")
        
class C(B):
    def m3(self):
        super().m2()
        print("Hello from m3() of Derived class 'C' ")

c1 = C()
c1.m3()
