
class A:
    def method1(self):
        print("Hello from method - 1 of Base class 'A' ")

class B:
    def method2(self):
        print("Hello from method - 2 of Base class 'B' ")

class C(A,B):
    def method3(self):
        print("Hello from method - 3 of Derived class 'C' ")

#creating object of DC C and calling its concrete and derived methods

c1 = C()
c1.method1()
c1.method2()
c1.method3()

