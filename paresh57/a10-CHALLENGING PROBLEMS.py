#SPY GAME:write a function that takes in a list of intigers and return true if it contains 007 in order.
#spy_game([1,2,4,0,0,7,5])==TRUE
#spy_game([1,0,2,4,0,5,7])==TRUE
#spy_game([1,7,2,0,4,5,0])==FALSE

def spy_game(nums):
    code=[0,0,7,'x']
    #[0,7,'x']
    #[7,'x']
    #['x'] length==1
    for num in nums:
        if num==code[0]:
            code.pop(0)
    return len(code)==1
print(spy_game([1,2,4,0,0,7,5]))
