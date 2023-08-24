import random
board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

currentPlayer = "X"
winner = None
gameRunning = True

# printing the game board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# take player input
def playerInput(board):
    inp = int(input("enter a number 1-9: "))
    if inp in range(1, 10):
        board[inp-1] = currentPlayer
    else:
        print("OOps, player is already in there")

# check for win or tie

def checkHorizontal(board):
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

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        print(board)
        print("its a tie")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkDiag(board) or checkHorizontal(board) or checkVertical(board):
        gameRunning = False
        print(f"The winner is {winner}")


# switch the player

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)

