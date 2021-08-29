# inheritance
class Parent(object):
    def __init__(self):
        print('\nparrent class constructor')

    def display(self):
        print('\nparrent class constructor')

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print('\nChild class constructor')

    def display(self):
        super(Child.self).display()
        print('\nChild class method')
p=Parent();
c=Child();
c.display();
