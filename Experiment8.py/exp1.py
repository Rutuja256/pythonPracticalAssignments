from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("area of Rectangle:",self.length* self.breadth)

class Dog:
    def __init__(self,name,bread):
        self.name = name
        self.bread = bread
    def bark(self):
        print("dog bark")
    def __del__(self):
        print("destructor called!") 
    def sound(self):
        print("Dog can make sound")     


class Student:
    def __init__(self,name,id,marks):
        self.name=name
        self.id=id
        self.marks=marks
    def show(self):
        print("student Name:",self.name) 
        print("student id:",self.id)
        print("student marks:",self.marks)


class BankAccount:
    def __init__(self,ballance):
        self.__ballance=ballance
    def getBallance(self):
        print("Bank Ballance:",self.__ballance)

class Cat:
    def sound(self):
        print("cat can make sound")

class Mobile :
    def __init__(self):
        self.model="samsung"
    def show(self):
        print(self.model) 

m=Mobile()
m.show()           


# b1=BankAccount(5000)
# b1.getBallance()  

# r1=Rectangle(8,6)
# r1.area()



# s1=Student("rutuja",1243,90)
# s2=Student("Shreya",578578,97)
# print(s1.name)
# s2.show()           
# d1=Dog("hari","b1")
# d2=Dog("max","b2")

# print(d1.name)
# print(d2.name)
# print(d1.bread)
# print(d2.bread)
# d1.bark()
# # del d2
# del d1
# print(d2.name)

# d1= Dog("max","golden")
# c1=Cat()
# c1.sound()
# d1.sound()




