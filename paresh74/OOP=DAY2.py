# __INIT__ METHOD

class Dog():
    def __init__(self,name):
        self.name=name
     #   print(f"the name of dog is {name}") #we can use self.name or name .also we can use print in line 11 to 15
    def add_one(self,x):
        return x+1         #see diffrence between using print and return
    def bark(self):
        print("bark")
d=Dog("raj")
print(d.name)
d2=Dog("bill")
print(d2.name)
