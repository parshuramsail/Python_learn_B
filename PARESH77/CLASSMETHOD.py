class Employee:
    increment=1.5
    no_of_employee=0
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        Employee.no_of_employee+=1

    def increse (self):
        self.salary=int(self.salary * self.increment)
        return self.salary

    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount


harry=Employee("'ra",22,20000)
raj=Employee("ani",12,1000)
print(harry.salary)
Employee.change_increment(3)
harry.increse()
print(harry.salary)
