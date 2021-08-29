# INHERITANCE ; CLASS DOG(ANIMALA)
class animal():
    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print(" I AM AN ANIMAL")

    def eat(self):
        print('I AM EATING')

class dog(animal):
    def __init__(self):
        animal. __init__(self)
        print('dog self')

    def who_am_i(self):
        print("dog is there ")

mydog=who_am_i(dog)

mydog=dog()
myanimal=animal()
myanimal.eat()
