# write a function that checks whether a number is in given range (inclusive of high and low).
def num_check(num,low,high):
     if num in range(low,high):
         print("%s in the range"%str(num))
     else:
         print('the number is outside the range')
print(num_check(3,1,10))
