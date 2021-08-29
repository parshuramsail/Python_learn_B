# USE OF SELF AND INIT
class employe:
    no_of_leaves=8
    def print_details(self):
        return f"the name is {self.name} ,salary is {self.salary} and role is {self.role}"
harry=employe()
rohan=employe()

harry.name="harry"
harry.salary=450
harry.role="ïnstructor"
rohan.name="rohan"
rohan.salary=333
rohan.role="student"
print(rohan.no_of_leaves)
print(rohan.__dict__ )
print(rohan.print_details()
