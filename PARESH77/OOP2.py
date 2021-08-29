# CREATING CLASS WITH CONSTRUCTOR
class Employee:
    def __init__(self,name,age,gender,salary):
        self.name=name
        self.age=age
        self.gender=gender
        self.salary=salary
    def employee_details(self):
        print(f"Employees Name is {self.name}")
        print(f"Age of Employee is{self.age}")
        print(f"Employees is {self.gender}")
        print(f"Employees salary is {self.salary}")
e1=Employee("Raj",21,"Male",15000)
e1.employee_details()
