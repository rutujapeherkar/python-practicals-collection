class A:
    def m1(self):
        print("Hello from m1() of BC 'A'")

class B(A):
    def m2(self):
        super().m1()
        print("Hello from m2() of DC 'B' ")

class C(A):
    def m3(self):
        super().m1()
        print("Hello from m3() of DC 'C' ")

b1 = B()
c1 = C()
b1.m2()
c1.m3()