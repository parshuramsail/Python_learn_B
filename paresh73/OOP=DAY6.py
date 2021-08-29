class emplooyee:
    no_of_leaves=8
    def __init__(self,name ,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def print_details(self):
        return f"THE NAME IS {self.name} .SALARY IS {self.salary} AND ROLE IS {self.role}"

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.new_leaves=new_leaves

    @classmethod
    def from_str(cls,string):
        pass

harry=emplooyee("HARRY",12000,"INSSTRUCTOR")
mohan=emplooyee("mOHAN",5444,"STUDENT")
karan=emplooyee.from_str("karan-3333-hero") #EMPLOYEE.FROM_STR ==== CLS,STRING

harry.change_leaves(33)
print(harry.no_of_leaves)
