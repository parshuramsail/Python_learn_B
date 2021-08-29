# CREATING OUR FIRST CLASS
#class Phone:
#    def make_call(self):
#        print("making a call")
#    def paly_game(self):
#        print("playing game")
#p1=Phone()
#p1.make_call()
#p1.paly_game()


# ADDING PARAMETER TO THE CLASS.
class Phone:
    def set_colour(self,colour):
        self.set_colour=colour
    def set_price(self,price):
        self.price=price
    def show_colour(self):
        return self.set_colour
    def show_price(self):
        return self.price
    def make_call(self):
        print("making a call")
    def play_game(self):
        print("playing game")
p2=Phone()
p2.set_colour("blue")
p2.show_colour()
p2.set_price(10000)
print(p2.show_price())
p2.play_game()
p2.make_call()
