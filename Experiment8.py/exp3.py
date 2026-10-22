
class Grandparent:
    def show_grandparent(self):
        print("This is the grandparent class")


class Parent(Grandparent):
    def show_parent(self):
        print("This is the parent class")


class Child(Parent):
    def show_child(self):
        print("This is the child class")


c = Child()
c.show_grandparent()
c.show_parent()
c.show_child()
