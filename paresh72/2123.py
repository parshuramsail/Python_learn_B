def dec1(function1):
    def execute():
        print("execute now")
        function1()
        print("here")
    return execute
#@dec1
def who():
    print("who is raj")
who()
