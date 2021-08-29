def function(*args,**kwargs):
    print(args)
    print(kwargs)
    return("i would like {} {}".format(args[0],kwargs['food']))
print(function(10,20,30,fruit='orange',food='eggs',animal="chicken"))
