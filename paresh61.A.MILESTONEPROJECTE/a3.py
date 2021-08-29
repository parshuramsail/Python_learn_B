# STEP3: Write a fuction  that takes in the board list object a marker(x or O),and desired position(numbers 1-9) and asssign it to the board.
def place_marker(board,marker,position):
    board [position]=marker
test_board=["#","X","O","X","O","X","O","X","O","X"]
place_marker(test_board,"$",8)
display_board(test_board)
