class dog():
    # attributes
    # we takes in the argument
    #assign it using self.attribute name

    def __init__(self,breed,name):
        self.breed=breed
        self.name=name

    #operations/ action ----> methods
    def bark(self):
        print("woof! my name is {}".format(self.name))
mydog=dog('lab','raj')

print(mydog.bark() )
