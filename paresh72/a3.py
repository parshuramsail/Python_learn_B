def hero(don):
    def zero():
        print("hero number1")
        don()
        don()
        print("zero number1")
    return zero
@hero
def mario(don):
    print("don number1")
mario()
