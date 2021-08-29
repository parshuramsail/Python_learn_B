#KWARGS
def m_function(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("i didnt find any fruit here")
print(m_function(fruit="apple",veg="potato"))

