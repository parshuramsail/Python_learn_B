class pet:
    def __init__(self,name,age):
       self.name=name
       self.age=age

    def show(self):
        print(f"I AM {self.name} AND I AM {self.age} YEAR OLD.")
        ;
class cat(pet):
    def speak(self):
        print("meow")
class dog(pet):
    def speak(self):
        print("bark")
p=pet("tim",19)
p.show()
