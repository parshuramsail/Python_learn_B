#LESSER OF TWO EVENS==write a function that returns the lesser of two given numbers if both numbers are even,but retrns the greater if both numbers are odd.
#lesser_of_two_evens(2,4)===2

#def lesser_two_evens(a,b):
#    if a%2==0 and b%2==0:
#        if a<b:
#            result=a
#        else:
#            result=b
#    else:
#        if a>b:
#            result=a
#        else:
#            result=b
#    return result
#print(lesser_two_evens(10,5))

#SHORT METHOD
def lesser_of_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        max(a,b)
print(lesser_of_evens(7,10))

