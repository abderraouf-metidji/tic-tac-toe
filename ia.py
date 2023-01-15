import random

signe = "O"

def ia(board, signe):
    while current_player == signe:
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = signe
            switch_player()
