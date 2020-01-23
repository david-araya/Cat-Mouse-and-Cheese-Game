from os import system

cat = -7
mouse = 1
cheese = 6

board = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
        
#def bestMoveCat(board,depth,mouse):

#def bestMoveMouse(board,depth,cat,cheese):

#def possibleMovesCat(board):

#def possibleMovesMouse(board):

def clearScreen():
    os = platform.system().lower()
    
    if 'windows' = os:
        os.sysem('cls')
    else :
        os.system('clear')

#def checkScore(board):
    
def checkWinner(board, player):
    if (player == 0 or player == 7)
        return True
        
    return False
    
def printBoard(board,mouse,cat,cheese):
    
#def mouseTurn(mouse,cat):

#def catTurn(cat,mouse):

#def checkScore():

#def move(x,y,player):


def main():

    if checkWinner(board, cat):
        clear_screen()
        print_board(board,mouse,cat,cheese)
        print ("CAT WINS")
        
    elif check_winner(board, mouse):
        clear_screen()
        print_board(board,mouse,cat,cheese)
        print ("MOUSE WINS")
    else:
        clear_screen()
        print_board(board,mouse,cat,cheese)
        print ("DRAW")

