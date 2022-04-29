#tic-tac-toe game.
#autor Kenny Castillo.

from colorama import init,Fore,Back,Style

def main():

       
    
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print(Style.BRIGHT + "Congratulations...You are awesome!. Thanks for playing!")
    print()
    print() 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    
    print()
    print(Style.BRIGHT + chr(27)+"[1;36m"+"-----Welcome to the Tic-Tac_Toe Game-----")
    print("First player will be 'X' and second player will be 'O'")
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print('--+---+---')
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print('--+---+---')
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()
    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
            


def make_move(player, board):

    
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player
    print("good choice!!")

    

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current ==  "x":
        return "o"

if __name__ == "__main__":
    main()

   
