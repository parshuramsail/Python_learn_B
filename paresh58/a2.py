# FILTER
def check_even(num):
    return num%2==0
my_number=[1,2,3,4,5,6]
filter(check_even,my_number)
for n in filter(check_even,my_number):
    print(n)
