class Employee:
    increment=2
    no_of_employee=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        Employee.no_of_employee+=1

    def increse(self):
        self.salary=int(self.salary*self.increment)

class Programer(Employee):
    def __init__(self,fname,lname,salary,proglang,exp):
        super().__init__(fname,lname,salary)
        self.proglang=proglang
        self.exp=exp

    def increse(self):
        self.salary=int(self.salary * (self.increment+0.2))
        return self.salary

    def __add__(self, other):
       return self.salary+other.salary
harry=Programer("harry","jackson",10000,"python",5)
raj=Programer("max","alpha",12000,"java",7)
a=6
print(a.__sub__(5))
print(harry+raj)
