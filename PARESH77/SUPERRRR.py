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
harry=Programer("harry","jackson",10000,"python",5)
print(harry.exp)
print(harry.salary)
print(harry.increse())

