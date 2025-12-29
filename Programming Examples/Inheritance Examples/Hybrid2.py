

class A:
    def m1(self):
        print("Hello from m1()")

class B(A):
    def m2(self):
        super().m1()
        print("Hello from m2()")


class D:
    def m3(self):
        print("Hello from m3()")

class C(B,D):
    def m4(self):
        super().m2()
        super().m3()
        print("Hello from m4()")

c1 = C()
c1.m4()