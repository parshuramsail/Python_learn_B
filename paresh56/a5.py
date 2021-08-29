def function(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("my choice of fruit is {}".format(kwargs['fruit']))
    else:
        print("i dont know")
print(function(fruit='apple',veg='potato'))
