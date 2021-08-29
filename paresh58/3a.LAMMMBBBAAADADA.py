# LAMBADA FUNCTION

square=lambda num:num**2
print(square(5))

#lambda map
my_nums=[1,2,3,4,5,5]
print(list(map(lambda num:num**2,my_nums)))


#lambda filter
my_nums=[1,2,3,4,5,5]
print(list(filter(lambda num:num**2,my_nums)))

#
names=['andy','candy','hero']
print(list(map(lambda x:x[::-1],names)))

#
names=['andy','candy','hero']
print(list(map(lambda x:x[0],names)))

#
names=['andy','candy','hero']
print(list(filter(lambda x:x[0],names)))
