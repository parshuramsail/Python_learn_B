# USING DEF FUNCTION AND SELF


#string="hello"
#print(string.upper())

#class Dog():
#    def bark(self):
#        print("bark")
#D=Dog()
#print(type(D))


#class Dog():
#    def bark(self):
#        print("bark")
#D=Dog()
#D.bark()

#using print

#class Dog():
#    def add_one(self,x):
#        print( x+1)          #see diffrence between using print and return.if you use print in line 21 then print is not required to use in line 26.
#    def bark(self):
#        print("bark")
#d=Dog()
#d.bark()
#d.add_one(5)

#using return

class Dog():
    def add_one(self,x):
        return x+1         #see diffrence between using print and return
    def bark(self):
        print("bark")
d=Dog()
d.bark()
print(d.add_one(5))    #if you use return in line 32 you havee to use print in line 37
