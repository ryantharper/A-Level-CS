from random import randint
from time import sleep
import sys

#list[row][col]
#grid = [[" "]*8 for i in range(9)]

def computerRand(board):
    print("Computer's Turn...")
    sleep(2)
    return randint(0,7)

# Function to see if player entere
def uIn(player):
    while True:
        try:
            ui = int(input(player + ": Enter a number between 1-8: "))
            if ui < 0 or ui > 8:
                print("You did not enter a number between 1 and 8")
            else:
                return ui
        except ValueError:
            print("You did not enter a number between 1 and 8")

# Winner Check Function
def winner(board):
    # Row
    for row in range(8):
        for col in range(5):
            if (board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]) and (board[row][col] != " "):
                return board[row][col]

    # Column 
    for col in range(8):
        for row in range(5):
            if (board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]) and (board[row][col] != " "):
                return board[row][col]

    # Diagonal Top Left to Bottom Right
    for row in range(5):
        for col in range(5):
            if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] ==board[row + 3][col + 3]) and (board[row][col] != " "):
                return board[row][col]

    # Diagonal Bottom Left to Top Right
    for row in range(7, 3, -1):
        for col in range(5):
            if (board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]) and (board[row][col] != " "):
                return board[row][col]
    # Check if board is full
    nv = 0
    for r in range(8):
        for c in range(8):
            if board[r][c] == " ":
                nv+=1
    if nv == 0:
        playAgain("TIE")

def printBoard(board):
    print("  1 2 3 4 5 6 7 8")
    for i in range(8):
        print(i+1, end='|')
        for c in range(8):
            print(board[i][c], end='|')
        print()

def cVpEasy():
    while True:
        p1D = uIn("P1")

        for x in range(7,-1,-1):
            if grid[x][p1D-1] == 'X' or grid[x][p1D-1] == 'O':
                continue
            else:
                grid[x][p1D-1] = 'X'
                break

        printBoard(grid)
        if winner(grid) == "X" or winner(grid) == "O":
            if winner(grid) == "X":
                playAgain("THE WINNER IS PLAYER 1")
                break
            else:
                playAgain("THE WINNER IS COMPUTER")
                break

        p2D = computerRand(grid)

        for x in range(7,-1,-1):
            if grid[x][p2D-1] == 'X' or grid[x][p2D-1] == 'O':
                continue
            else:
                grid[x][p2D-1] = 'O'
                break

        printBoard(grid)
        if winner(grid) == "X" or winner(grid) == "O":
            if winner(grid) == "X":
                playAgain("THE WINNER IS PLAYER 1")
                break
            else:
                playAgain("THE WINNER IS COMPUTER")
                break

def cVpHard():
    while True:
        p1D = uIn("P1")

        for x in range(7,-1,-1):            
            if grid[x][p1D-1] == 'X' or grid[x][p1D-1] == 'O':
                continue
            else:
                grid[x][p1D-1] = 'X'
                break
  
        if winner(grid) == "X" or winner(grid) == "O":
            if winner(grid) == "X":
                playAgain("THE WINNER IS PLAYER 1")
                printBoard(grid)
                break
            else:
                playAgain("THE WINNER IS COMPUTER")
                printBoard(grid)
                break

        p2D = computerRand(grid)
                
        for x in range(7,-1,-1):
            if grid[x][p2D-1] == 'X' or grid[x][p2D-1] == 'O':
                continue
            else:
                grid[x][p2D-1] = 'O'
                print("AI PLACED IT AT COLUMN:", p2D, "ROW:",x)
                break
        
        if winner(grid) == "X" or winner(grid) == "O":
            if winner(grid) == "X":
                playAgain("THE WINNER IS PLAYER 1")
                printBoard(grid)
                break
            else:
                playAgain("THE WINNER IS COMPUTER")
                printBoard(grid)
                break

def cVpNightmare():
        while True:
            p1D = uIn("P1")

            for x in range(7,-1,-1):
                if grid[x][p1D-1] == 'X' or grid[x][p1D-1] == 'O':
                    continue
                else:
                    grid[x][p1D-1] = 'X'
                    break

            
            if winner(grid) == "X" or winner(grid) == "O":
                if winner(grid) == "X":
                    playAgain("THE WINNER IS PLAYER 1")
                    printBoard(grid)
                    break
                else:
                    playAgain("THE WINNER IS COMPUTER")
                    printBoard(grid)
                    break

            p2D = computerRand(grid)

            for x in range(7,-1,-1):
                if grid[x][p2D-1] == 'X' or grid[x][p2D-1] == 'O':
                    continue
                else:
                    grid[x][p2D-1] = 'O'
                    break
            
            if winner(grid) == "X" or winner(grid) == "O":
                if winner(grid) == "X":
                    playAgain("THE WINNER IS PLAYER 1")
                    printBoard(grid)
                    break
                else:
                    playAgain("THE WINNER IS COMPUTER")
                    printBoard(grid)
                    break

def pvp():
    while True:
        p1D = uIn("P1")
        for x in range(7,-1,-1):
            if grid[x][p1D-1] == 'X' or grid[x][p1D-1] == 'O':
                continue
            else:
                grid[x][p1D-1] = 'X'
                break

        printBoard(grid)
        if winner(grid) == "X" or winner(grid) == "O":
            if winner(grid) == "X":
                playAgain("THE WINNER IS PLAYER 1")
                break
            else:
                playAgain("THE WINNER IS PLAYER 2")
                break
        
        p2D = uIn("P2")

        for x in range(7,-1,-1):
            if grid[x][p2D-1] == 'X' or grid[x][p2D-1] == 'O':
                continue
            else:
                grid[x][p2D-1] = 'O'
                break

        printBoard(grid)
        if winner(grid) == "X" or winner(grid) == "O":
            if winner(grid) == "X":
                playAgain("THE WINNER IS PLAYER 1")
                break
            else:
                playAgain("THE WINNER IS PLAYER 2")
                break
    
def playAgain(winner):
    print(winner)
    play_again = str(input("Would you like to play again?\n>>> "))
    if play_again.lower().startswith('y'):
        grid=[]
        start()
    else:
        sys.exit(0)

def start():
    global grid
    grid = [[" "]*8 for i in range(9)] # Initialise grid using list comprehension
    game = int(input("Would you like to\n1. Player Vs Player\n2. Computer vs Player (EASY)\n3. Computer vs Player (HARD)\n4. Computer vs Player (NIGHTMARE)Please enter the number that corresponds with the option. (Player 1 = X, Player 2 = O)"))
    if game == 1:
        pvp()
    elif game == 2:
        cVpEasy()
    elif game == 3:
        cVpHard()
    elif game == 4:
        cVpNightmare()

start()
