#FIND 33:
#given a list of inits,return True if the array contains a 3 next too 3 somewhere.
#has_33([1,3,3])==True
#has_33([1,3,1,3])==false
#has_33([3,1,3])==false

def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False
print(has_33([1,3,3]))

#method2
def has_33(nums):
    for i in range(0,len(nums)):
        if nums[i:i+1]==[3,3]:
            return True
    return False
print(has_33([1,3,3]))
