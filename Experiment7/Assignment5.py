
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Person Name:", self.name)


class Student(Person):
    def display(self):
        print("Student Name:", self.name)


s1 = Student("Rutuja")
s1.display()
