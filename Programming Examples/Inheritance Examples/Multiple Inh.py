class A:
    a = None
    def __init__(self,a):
        self.a = a
        print("Constructor of class A")
    def method1(self):
        print("Method1 of class A")
        print("Value of a is :", self.a)

    def __del__(self):
        print("Destructor of class A")

class B:
    b = None
    def __init__(self, b):
        print("Constructor of class B")
        self.b = b

    def method1(self):
        print("Method1 of class B")
        print("Value of b :", self.b)

    def __del__(self):
        print("Destructor of class B")

class C(A,B):
    c = None
    def __init__(self,a,b,c):
        A.__init__(self, 10)
        B.__init__(self, 20)
        print("Constructor of class C\n")
        self.c = c

    def method1(self):
        A.method1(self)
        B.method1(self)
        print("Method1 of class C")
        print("Value of c :", self.c)

    def __del__(self):
        A.__del__(self)
        B.__del__(self)
        print("Destructor of class C")

c1 = C(10,20,30)
c1.method1()
