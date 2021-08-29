#normal def
#def function(a,b,c=0,d=1):
#    return sum((a,b))*0.05
#print(function(3,4))

#USING ARGS

def function(*args):
    return sum(args)*0.05
print(function(4,6))
