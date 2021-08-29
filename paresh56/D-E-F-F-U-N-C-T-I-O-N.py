#def dog_function(mystring):
#    if 'dog' in mystring:
#        return True
#    else:
#        return False
#print(dog_function("dog run away"))


def dog_function(mystring):
    return 'dog' in mystring.lower()
c=dog_function("Dog ran away")
print(c)
