def dec1(fun1):
    def example():
        print("you are first")
        fun1()
        print("you are first")
        fun1()
    return example
def who_are_you():
    print("you are second")
who_are_you=dec1(who_are_you)
who_are_you()
