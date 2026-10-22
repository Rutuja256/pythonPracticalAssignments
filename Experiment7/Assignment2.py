
class Student:
    def __init__(self, name="Unknown", roll_no=0):
        self.name = name
        self.roll_no = roll_no
        print("Constructor called")

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)


# Default values
s1 = Student()
s1.display()

print()

# Parameterized initialization
s2 = Student("Rutuja", 101)
s2.display()
