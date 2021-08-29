#BLACKJACK:given three intigers between 1 and 11,if thier sum is less than or equal to 21,return their sum.
#if there sum is exeeds 21 and thers an eleven,reduce sum by 10.finally if the sum(even after adjustments) exeeds 21,return "BUST".
#black_jack(5,6,7)==18
#black_jack(9,9,9)==BUST
#black_jack(9,9,11)==19

def blackjack(a,b,c):
    if sum([a,b,c])<=21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c])<=31:
        return sum([a,b,c])-10
    else:
        return "BUST"
print(blackjack(10,10,11))
