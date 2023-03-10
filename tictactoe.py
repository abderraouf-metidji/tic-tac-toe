import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

current_player = "X"
winner = None
game_running = True


#Affichage du jeu vide

def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#Input du joueur 1

def player_input(board):
    inp = int(input("Entrer un nombre de 1 a 9 : "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print("Case invalide merci de reessayer")

#Verirfication de l"etat de jeu (victoire - defaire - match nul)

def check_horizental(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    if board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def check_tie(board):
    global game_running
    if "-" not in board and winner == False:
        print_board(board)
        print("Match nul ! ")
        game_running = False

def check_win():
    if check_diagonal(board) or check_horizental(board) or check_row(board):
        print(f"Le gagnant est : {winner} ! ")

#Input du joueur 2

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

#Verirfication de l"etat de jeu (victoire - defaire - match nul)

while game_running:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
    ia(board, signe)
    check_win()
    check_tie(board)