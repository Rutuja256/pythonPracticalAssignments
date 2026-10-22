
class Father:
    def skill1(self):
        print("Father knows gardening")


class Mother:
    def skill2(self):
        print("Mother knows cooking")


class Child(Father, Mother):
    def skill3(self):
        print("Child knows programming")


c = Child()
c.skill1()
c.skill2()
c.skill3()
