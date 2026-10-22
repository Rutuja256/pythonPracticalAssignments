
class Demo:
    def __init__(self):
        print("Constructor called")

    def display(self):
        print("Object is working")

    def __del__(self):
        print("Destructor called")


print("Creating object")

obj = Demo()
obj.display()

print("Deleting object")

del obj

print("Program completed")
