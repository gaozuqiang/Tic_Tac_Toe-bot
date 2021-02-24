hu_letter='x'  
com_letter='o'
def drawBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '
    print('What is your next move? (1-9)')
    move = int(input())
    if (board[move]!= ' '):
        print('the spot is not empty plz choose another one ')
        getPlayerMove(board)
    else:
        board[move]=hu_letter
        if (winner(board,hu_letter)):
            print('player win')

def winner(bo,le):
    if (bo[1]==le and bo[2]== le and bo[3]==le): #across top
        return True
    elif (bo[4]==le and bo[5]== le and bo[6]==le): #across middle
        return True
    elif (bo[7]==le and bo[8]== le and bo[9]==le): #bottom
        return True
    elif (bo[1]==le and bo[4]== le and bo[7]==le): #columun 1
        return True
    elif (bo[2]==le and bo[5]== le and bo[8]==le): #colum 2
        return True
    elif (bo[3]==le and bo[6]== le and bo[9]==le): #colmun 3
        return True
    elif (bo[1]==le and bo[5]== le and bo[9]==le): #diagonal 
        return True
    elif (bo[3]==le and bo[5]== le and bo[7]==le): #diagonal
        return True

def draw(board):
    for i in range(1,10):
        if (board[i]==' '):
            return False
    return True

def statue(board): 
    if (winner(board,hu_letter)):
        return True
    elif (winner(board,com_letter)):
        return True
    elif (draw(board)):
        return True

def compMove(board):
    bestScore = -1000
    bestMove = 0
    for i in range(1,10):
        if (board[i] == ' '):
            board[i] = com_letter
            score = minimax(board, 0, False)
            board[i] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = i

    board[bestMove]=com_letter
    return


def minimax(board, depth, isMaximizing):
    if (winner(board,com_letter)):
        return 1
    elif (winner(board,hu_letter)):
        return -1
    elif (draw(board)):
        return 0

    if (isMaximizing):
        bestScore = -1000
        for i in range(1,10):
            if (board[i] == ' '):
                board[i] = com_letter
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 1000
        for i in range(1,10):
            if (board[i] == ' '):
                board[i] = hu_letter
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore
theboard=[' ']*10


drawBoard(theboard)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")

while not statue(theboard):
    compMove(theboard)
    drawBoard(theboard)
    if statue(theboard):
        if draw(theboard):
            print('draw')
        elif winner(theboard,com_letter):
            print('bot win')
        break
    getPlayerMove(theboard)
    drawBoard(theboard)
    if statue(theboard):
        if draw(theboard):
            print('draw')
        break 
