#COUNT PRIMES:WRITE A FUNCTION THAT RETURNS THE NUMBERS OF PRIME NUMBERS THAT EXIST UP TO AND INCLUDING A GIVEN NUMBER.
#by convention well treat 0 and 1 as not prime.

def counter_primes(num):
    # check for 0 or 1 input
    if num<2:
        return 0

    # 2 or greatr
    # store primenumbers
    primes=[2]

    #counter going upto the input number
    x=3

    # x is going through every number upto input number
    while x<=num:

        # check if x is prime
        for y in range(3,x,2):
            if x%y==0:
                x+=2
                break
        else:
            primes.append(x)
            x+=2
    print(primes)
    return (len(primes))
print(counter_primes(100))

