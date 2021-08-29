class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_vehicle_details(self):
        print("I am a Vehicle")
        print(f"mileage of Vehicle is {self.mileage}")
        print(f"cost of Vehicle is {self.cost}")
class Car(Vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres=tyres
        self.hp=hp
    def show_car_details(self):
        print("number of tyres in car",self.tyres)
        print("horse power of car is",self.hp)
        print("i am car")
c1=Car(100,500000,4,90)
c1.show_car_details()
c1.show_vehicle_details()

# EXAMPLE2:
class Phone:
    def __init__(self,ram,processor):
        self.ram=ram
        self.processor=processor
    def show_phone_details(self):
        print(f"mobile is {self.ram} gb ram variant ")
        print(f"it consist of {self.processor} processor")
class Moto(Phone):
    def __init__(self,ram,processor,camera,cost):
        super().__init__(ram,processor)
        self.camera=camera
        self.cost=cost
    def show_moto_details(self):
        print(f"it consist of{self.camera} camera ")
        print(f"th phones cost is  { self.cost}")
g1=Moto(8,"snap dragon","64  mega pixels",20000)
g1.show_phone_details()
g1.show_moto_details()
