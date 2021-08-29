
class Employee:
    increment=2000
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def show_details(self):
        self.salary=int(self.salary * self.increment)
        return self.salary
harry=Employee("'ra",22,20000)
print(harry.show_details())
raj=Employee("ani",12,1000)
print(Employee.__dict__)


# EXAMPLE2:
class Employee:
    increment=2000
    no_of_employee=0
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        Employee.no_of_employee+=1
    def show_details(self):
        self.salary=int(self.salary * self.increment)
        return self.salary
print(Employee.no_of_employee)
harry=Employee("'ra",22,20000)
print(harry.show_details())
raj=Employee("ani",12,1000)
print(Employee.__dict__)
