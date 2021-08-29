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

    @staticmethod
    def isopen(day):
        if day=="sunday":
            return "NO"
        else:
            return "YES"

print(Employee.isopen("sunday"))
harry=Employee("ram",22,20000)
print(harry.isopen("monday"))
