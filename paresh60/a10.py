 # INHERITANCE

class Parent():
    def __init__(self,last_name,eye_colour):
        self.last_name=last_name
        self.eye_colour=eye_colour

    def show_info(self):
        print(self.last_name + "eye colour is" + self.eye_colour)

class Child(Parent):
    def __init__(self,last_name,eye_colour,number_of_toyes):
        Parent.__init__(self,last_name,eye_colour)
        self.number_of_toyes=number_of_toyes

    def show_info(self):
        print(self.last_name + " eye colour is " + self.eye_colour + " and no of toys are " + str(self.number_of_toyes))

Avinash=Parent("Shetty","Brown")

Rahul=Child("shetty","Black",5)
Avinash.show_info()
Rahul.show_info()
print(Avinash.eye_colour)
print(Rahul.eye_colour)
