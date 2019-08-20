
# There are 4 types of polymorphism
# 1. Duck Typing
# 2. Operator Overloading
# 3. Method Overloading
# 4. Method Overriding

############################ Duck Typing ##################################

# Duck typing in computer programming is an application
# of the duck test—"If it walks like a duck and it quacks
# like a duck, then it must be a duck"—to determine if an
# object can be used for a particular purpose. With normal
# typing, suitability is determined by an object's type.

print("############################ Duck Typing ##################################")

class Laptop:

    def code(self,ide):
        ide.execute()


class PyCharm:

    def execute(self):
        print("PyCharm Compiling Code in your Laptop...")
        print("PyCharm Running Code in your Laptop...")

class Java:

    def execute(self):
        print("Java Compiling Code in your Laptop...")
        print("Java Running Code in your Laptop...")


ide1 = PyCharm()
ide2 = Java()

l1 = Laptop()
l1.code(ide1)   # Pycharm execute called
l1.code(ide2)   # Java execute called


############################ Operator Overloading ##################################

print("############################ Operator Overloading ##################################")

class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):       # Overload add operator
        t1 = self.m1 + other.m1
        t2 = self.m2 + other.m2
        t = Student(t1, t2)
        return t

    def __str__(self):              # Overload object printing operator
        return ("{} {}".format(self.m1, self.m2))

    def __gt__(self, other):        # Overload greater than operator
        t1 = self.m1 + self.m2
        t2 = other.m1 + other.m2
        if t1 > t2:
            return True
        else:
            return False


s1 = Student(100, 90)
s2 = Student(90, 90)
print(s1)       # __str__ called
print(s2)       # __str__ called
s3 = s1 + s2    # __add__ called
print(s3)       # __str__ called

if s1 > s2:     # __gt__ called
    print("s1 is greater than s2")
else:
    print("s2 is greater than s1")

############################ Method overloading ##################################

print("############################ Method overloading ##################################")

class SumSample:

    def sum(a=None, b=None, c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a

        return s

s1 = SumSample
print(s1.sum(10))


############################ Method overriding ##################################

print("############################ Method overriding ##################################")


class A:

    def show(self):
        print("Show of class A")


class B(A):

    def show(self):     # show method overridden
        print("Show of class B")


b = B()
b.show()    # overridden method called

