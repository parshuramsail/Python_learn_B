#ALMOST THERE:given an intiger n,return true if n is within 10 of either 100 and 200
#almost_there(90)==true
#almost_there(120)==false
#almost_there(99)==true
#almost_there(209)==true

def almost_there(n):
    return (abs(100-n)<=10) or (abs(200-n)<=10)
print(almost_there(91))
