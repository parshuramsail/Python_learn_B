# WE CAN USE THIS FOR SOME LITTLE RANGE ONLY.

class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return  self.name
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age=age
d=Dog("tim",5)
d.set_age(8)
print(d.get_age())


