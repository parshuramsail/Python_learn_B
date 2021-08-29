class employee():
    no_of_leaves=12
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def details(self):
        return f"the name is {self.name},salary is {12000} and role is {self.role}"
    @classmethod
    def change_leaves
