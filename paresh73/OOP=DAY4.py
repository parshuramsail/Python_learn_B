    # USE OF SELF AND INIT
class employe:
    no_of_leaves=8
    def print_details(self):
        return f"the name is {self.name} ,salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls,new_leaaves):
        cls.no_of_leaves=new_leaaves
harry=employe()
rohan=employe()

harry.name="harry"
harry.salary=450
harry.role="ïnstructor"

rohan.name="rohan"
rohan.salary=333
rohan.role="student"
harry.change_leaves(55)

print(harry.no_of_leaves)
print(rohan.__dict__ )
