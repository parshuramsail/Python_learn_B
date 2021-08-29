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
