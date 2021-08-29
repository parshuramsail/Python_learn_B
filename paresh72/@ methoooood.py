def dec1(func1):
    def execute():
        print("you are first")
        func1()
        print("you are second")
        func1()
        func1()
    return execute
@dec1
def who_ar_you():
    print("you are briliant")
#who_ar_you=dec1(who_ar_you)   #  @ method
who_ar_you()
@dec1
def add():
    print("sum is",2+2)
add()
