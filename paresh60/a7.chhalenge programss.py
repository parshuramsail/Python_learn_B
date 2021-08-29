class acount():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,dep_amount):
        self.balance=self.balance+dep_amount
        print(f'added {dep_amount} to the balance')

    def withdrawal(self,wd_amount):
        if self.balance>=wd_amount:
            self.balance=self.balance-wd_amount
            print('withdrawal accepted')

        else:
            print("sorry non enough funds!")

    def __str__(self):
        return f'owner:{self.owner}\nBalance:{self.balance}'

a=acount('sam',500)
#print(a.owner)
#print(a.balance)
print(a)
print(a.withdrawal(d ))
