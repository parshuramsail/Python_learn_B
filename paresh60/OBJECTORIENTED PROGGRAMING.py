class dog():
    # attributes
    # we takes in the argument
    #assign it using self.attribute name

    def __init__(self,breed,name,spots):
        self.breed=breed
        self.name=name
        self.spots=spots
mydog=dog(breed='lab',name='raj',spots='no spots')

print(mydog.breed,mydog.spots )


#attributes
class dog():

    speices='mammal'
    def __init__(self,breed,name,spots):
        self.breed=breed
        self.name=name
        self.spots=spots
mydog=dog(breed='lab',name='raj',spots='no spots')

print(mydog.breed,mydog.spots )
print(mydog.speices)
