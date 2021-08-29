# INHERITANCE IN OOP.
class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print("I am a Vehicle")
        print(f"mileage of Vehicle is {self.mileage}")
        print(f"cost of Vehicle is {self.cost}")
class Car(Vehicle):
    def show_car(self):
        print("I am a car")
c1=Car(200,120000)
c1.show_details()
c1.show_car()

# example2:
class computer:
    def __init__(self,ram,storage,processor):
        self.ram=ram
        self.storage=storage
        self.processor=processor
    def show_details(self):
        print("iam a laptop")
        print(f"{self.ram}gb ram")
        print(f"processor is {self.processor}")
class laptop(computer):
    def show_laptop(self):
        print("this is laptop")
b1=laptop(8,"1tb","amd")
b1.show_details()
