# Inheritance
# Some important points for __init__ method in inheritance
# 1. If you create object of Sub class it will first try find init of Sub class
#    if it is not found then it will call init of Super class
# 2. When you create object of Sub class it will call init of Sub class first
#    if you have call super then it will first call init of Super class then call init of Sub class


# Multilevel Inheritance
# A
# ^
# |
# B
# ^
# |
# C


class A:    # Parent Class / Super Class

    def __init__(self):
        print("Class A __inti__")

    def feature1(self):
        print("Feature 1 Working...")

    def feature2(self):
        print("Feature 2 Working...")


print("Object of A")
a1 = A()
a1.feature1()
a1.feature2()


class B(A):  # Child Class / Sub Class of A

    def __init__(self):
        super().__init__()      # __init__ of parent class is called
        print("Class B __inti__")

    def feature3(self):
        print("Feature 3 Working...")

    def feature4(self):
        print("Feature 4 Working...")


print("Object of B")
b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()


class C(B):   # Child Class / Sub Class of B

    def __init__(self):
        super().__init__()
        print("Class C __init__")

    def feature5(self):
        print("Feature 5 Working...")

print("Object of C")
c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

print("#############################################")

# Multiple Inheritance
#   X   Y
#    \ /
#     v
#     |
#     Z


class X:    # Parent Class / Super Class

    def __init__(self):
        print("Class X __inti__")

    def feature1(self):
        print("Feature 1 Working...")

    def feature2(self):
        print("Feature 2 Working...")


class Y:    # Parent Class / Super Class

    def __init__(self):
        print("Class Y __inti__")

    def feature3(self):
        print("Feature 3 Working...")

    def feature4(self):
        print("Feature 4 Working...")


class Z(X,Y):    # Parent Class / Super Class

    def __init__(self):
        super().__init__()
        print("Class Z __inti__")

    def feature5(self):
        print("Feature 5 Working...")

    def feature6(self):
        print("Feature 6 Working...")


z1 = Z()
z1.feature1()
z1.feature2()
z1.feature3()
z1.feature4()
z1.feature5()