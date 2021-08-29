#MULTILEVEL INHERITANCE
class Parent:
    def assign_name(self,name):
        self.name=name
    def show_name(self):
        return self.name

class Child(Parent):
    def assign_age(self,age):
        self.age=age
    def show_age(self):
        return self.age

class GrandChild(Child):
    def assign_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        return self.gender
g=GrandChild()
g.assign_name("raj")
g.assign_age(23)
g.assign_gender("male")
print(g.show_name())
print(g.show_age())
print(g.show_gender())
