
# Types of Variable
# 1. Instance Variable
# 2. Class Variable

# Types of methods
# 1. Instance Method
# 2. Class Method
# 3. Static Method


class Car:

    num_of_wheels = 4               # Class Variable

    def __init__(self):
        self.model = "Null"         # Instance Variable
        self.mileage = "0"          # Instance Variable

    def display(self):              # Instance Method
        print("Model :", self.model)
        print("Mileage :", self.mileage)

    @classmethod                    # Class Method Decorator
    def num_of_wheels_method(cls):           # Class Method
        print("Number of wheels :", cls.num_of_wheels)

    @staticmethod                   # Static Method Decorator
    def info():                     # Static Method
        print("This is a Car Class...")


c1 = Car()
c2 = Car()

# Object c1
c1.display()
print("*******************************")
c1.model = "BMW"
c1.mileage = 40
c1.display()

print("###############################")

# Object c2
c2.display()
c2.model = "Mercedez"
c2.mileage = 45
print("*******************************")
c2.display()

print("###############################")

# Change Instance Variable

Car.num_of_wheels = 5       # To make change in all objects instances, access it using Class_name.Variable_name

c1.display()
c2.display()

print("###############################")

# Call different Methods
print("Call different methods")
c1.display()    # Instance Method
Car.num_of_wheels_method()    # Class Method
Car.info()    # Static Method