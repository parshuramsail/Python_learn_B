# STEP1: write a function that can printout a board.setup your board as your list,where each index 1-9 corresponnds with a number on a numberpad.
#so you can get a 3 by 3 board representation.

#print('\n'*100)
def display_board(board):
    print('\n'*100)
    print("     |        |")
    print("   " +     board[7] + '  |  ' +      board[8]      +      '      |  ' + board[9])
    print("     |        |")
    print("--------------------")
    print("     |        |")
    print("   " +     board[4] + '  |  ' +      board[5]      +      '      |  ' + board[6])
    print("     |        |")
    print("--------------------")
    print("     |        |")
    print("   " +     board[1] + '  |  ' +      board[2]      +      '      |  ' + board[3])
    print("     |        |")

# TEST STEP1:RUN YOUR FUNCTION ON TEST VERSION OF THE BOARD LIST AND MAKE ADJUSTMENTS AS NECESSARY.

test_board=["#","X","O","X","O","X","O","X","O","X"]
#test_board=['']*10
display_board(test_board)
#print(display_board(test_board))

# STEP3:

def player_input():
    """
    output:(player1=marker, player2=marker)
    """
    marker=""
    # keep asking player 1 to choose X or O

    while marker!="X" and marker!="O":
        marker=input("player:1 choose X or O: ").upper()

    if marker=="X":
        return("X","O")
    else:
        return("O","X")

# RUN THE FUNCTION TO MAKE SURE IT RUNS THE DESIRED OUTPUT

player1_marker,player2_marker=player_input()

# STEP3
def place_marker(board,marker,position):
    board [position]=marker
test_board=["#","X","O","X","O","X","O","X","O","X"]
place_marker(test_board,"$",8)
display_board(test_board)

# STEP 4: WRITE IN A FUNCTION THAT TAKES IN A BOARD AND MARK (X OR O) AND CHECKS TO SEE IF THAT MARK HAS WON.
def win_check(board,mark):

    return((board[7]==mark and board[8]==mark  and board[9]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark)or
    (board[1]==mark and board[2]==mark and board[3]==mark)or
    (board[7]==mark and board[4]==mark and board[1]==mark)or
    (board[8]==mark and board[5]==mark and board[2]==mark)or
    (board[9]==mark and board[6]==mark and board[3]==mark)or
    (board[7]==mark and board[5]==mark and board[3]==mark)or
    (board[9]==mark and board[5]==mark and board[1]==mark))

win_check(test_board,"X")
