def dec1(func1):
    def nowexec():
        print("EXECUTING NOW")
        func1()
        print("ëxecuted")
    return nowexec
@dec1
def who_is_raj():
    print("raj is good boy")
#who_is_raj=dec1(who_is_raj)   # instead this use @dec1 in line 7
who_is_raj()
