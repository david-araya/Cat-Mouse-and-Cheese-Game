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
    
    if 'windows' in os:
        os.sysem('cls')
    else:
        os.system('clear')

#def checkScore(board):
    
def checkWinner(board, player):
    if player == 0 or player == 7:
        return True
        
    return False
    
#def printBoard(board,mouse,cat,cheese):
    
#def mouseTurn(mouse,cat):

#def catTurn(cat,mouse):

#def checkScore():

#def move(x,y,player):

def main():
    play = "Y"
    while play.upper() == "Y":
        clearScreen()
    
        if checkWinner(board, cat):
            clearScreen()
            printBoard(board,mouse,cat,cheese)
            print("CAT WINS")
    
        elif checkWinner(board, mouse):
            clearScreen()
            printBoard(board,mouse,cat,cheese)
            print("MOUSE WINS")
    
        else:
            clearScreen()
            printBoard(board,mouse,cat,cheese)
            print("DRAW")
        play = input("Play again? y/n: ")
    
    exit()

        
