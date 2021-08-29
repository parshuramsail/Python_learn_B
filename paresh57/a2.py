#MAKES TWENTY Given two intigers,return true if the sum of the intigers 20 or one of intigers is 20.if not retuurn false.
#makes_twenty(20,10)===true
#makes-twentyy(12,8)===true
#makestwenty(2,3)===false

def makes_twenty(a,b):
    if  a==20 or b==20 or a+b==20:
        return True
    else:
        return False
print(makes_twenty(8,12))
