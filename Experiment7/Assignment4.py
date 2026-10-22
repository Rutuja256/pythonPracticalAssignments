
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        print("Rectangle object created")

    def calculate_area(self):
        return self.length * self.breadth

    def display(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area:", self.calculate_area())

    def __del__(self):
        print("Rectangle object destroyed")


# Creating an object
r1 = Rectangle(10, 5)

# Displaying rectangle details
r1.display()

# Destroying the object reference
del r1
