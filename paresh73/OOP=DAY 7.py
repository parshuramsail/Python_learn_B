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
    def from_dash(cls,string):
       # param=str.split("-")  #SPLIT== IS PRODUCE OUTPUT IN LISTS.
       # print(param)
       # return cls(param[0],param[1],param[2])
        return cls(*string.split("-"))   #ONLINER CODE ABOVE 3 LINES ARE COMMENT OUT

harry=emplooyee("HARRY",12000,"INSSTRUCTOR")
mohan=emplooyee("mOHAN",5444,"STUDENT")
karan=emplooyee.from_dash("karan-3333-hero") #EMPLOYEE.FROM_STR ==== CLS,STRING

harry.change_leaves(33)
print(harry.no_of_leaves)
