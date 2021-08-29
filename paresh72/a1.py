def dec1(func1):
    def nowexec():
        print("EXECUTING NOW")
        func1()
        print("ëxecuted")
    return nowexec()
def who_is():
    print("who are you")
who_is=dec1(who_is)
who_is()
