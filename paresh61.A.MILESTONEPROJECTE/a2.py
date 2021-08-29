# STEP2: Write a function that can  take in a player input and assign their marker as a "x" or "O".
# Think about using while loops to continuesly ask until you get a correct answer.
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


