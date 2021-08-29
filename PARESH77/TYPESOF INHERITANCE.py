# SINGLE INHERITANCE
# MULTIPLE INHERITANCE
# MULTI LEVEL INHERITANCE
# HYBRID INHERITANCE

# MULTIPLE INHERITANCE IN ONE
class Parent1:
    def assign_one(self,str1):
        self.str1=str1
    def show_assign_one(self):
        return self.str1

class Parent2:
    def assign_two (self,str2):
        self.str2=str2
    def show_assign_two(self):
        return self.str2

class Child(Parent1,Parent2):
    def assign_three(self,str3):
        self.str3=str3
    def show_assign_three(self):
        return self.str3
c=Child()
c.assign_one("i am a parent 1")
c.assign_two(" iam a parent2 ")
c.assign_three("i am a child")
print(c.show_assign_one())
print(c.show_assign_two())
print(c.show_assign_three())
