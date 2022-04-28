#CSE-210; Week02
#Tic-Tac-Toe
#Tonatiuh Gonzalez

from colored import fg, bg, attr                #Library to print colored text

def Create_Board():
    board = []                                  #Creates an empty list
    for square in range(9):                     #Creates 9 squares
        board.append(square + 1)                #As iterator goes through, it will add one square to the list
    return board

def Display_Board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]} ")
    print(f"+ - + - +")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print(f"+ - + - +")
    print(f"{board[6]} | {board[7]} | {board[8]} ")
    print()

def main():
    print ('%s Hello World !!! %s' % (fg(1), attr(0)))
    player = next_player("")                        #Start game 
    board = Create_Board()                          #Call Create_Board() and assign a value to it, so it can be used as a parameter
    while not (draw(board) or winner(board)):       #While there is not a draw nor a winner
        Display_Board(board)                        #Call Display_board
        play_turn(player, board)                    #Give turn to next player
        player = next_player(player)                #The value that player chose will be replaced by an x or an o
    Display_Board(board)
    print("You won! Start the game again")      
    
def play_turn(player, board):                                               
    playerschoice = int(input(f"{player}'s turn to choose a square from 1-9: "))     #The player will choose a square to place its game-piece
    board[playerschoice - 1] = player                                                #The player's selection will be in the selected number0

def next_player(currentplayer):                             #CurrentPlayer starts as "" so this will allow to change between players with x's and o's 
    if (currentplayer) == "" or currentplayer == "o":
        return "x"
    elif currentplayer == "x":                              #CurrentPlayer will change to "o" when "x" turn is over
        return "o"

def draw(board): 
    for square in range(9):                                 #Iterator will go through each square in the board
        if board[square] != "x" and board[square] != "o":   #If there is a square with no x or o, the game is still going
            return False                                    #THe game is not over
    return True                                             #If there are no squares with numbers left, it is a tie

def winner(board):                                          #All Options in which a player can win
    if board[0] == board [1] == board[2]:
        return True
    elif board[3] == board [4] == board[5]:
        return True
    elif board[6] == board [7] == board[8]:
        return True
    elif board[0] == board [3] == board[6]:
        return True
    elif board[1] == board [4] == board[7]:
        return True
    elif board[2] == board [5] == board[8]:
        return True
    elif board[0] == board [4] == board[8]:
        return True
    elif board[2] == board [4] == board[6]:
        return True

main()