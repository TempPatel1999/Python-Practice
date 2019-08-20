# Inner Class sample
# You can create object of inner class inside the outer class
# Or
# You can create object of inner class outside the outer class
# provided you use outer class name to call it


class Student:

    def __init__(self,name,roll_no):

        self.name = name
        self.roll_no = roll_no
        # Inner Class object created in Outer Class
        self.laptop = Student.Laptop()

    def show(self):
        print("Name :", self.name)
        print("Roll number :", self.roll_no)
        self.laptop.show()

    class Laptop:

        def __init__(self):
            self.brand = "Asus"
            self.model = "ROG"

        def show(self):
            print("Brand :", self.brand)
            print("Model :", self.model)


s1 = Student("Maharshi", 71)
s1.show()

# Inner class object created outside outer class
s2 = Student.Laptop()
s2.show()