import random


def drawBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Choose what to be: X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Choosing the first to play: Randomly
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def makeMove(board, letter, move):
    board[move] = letter


def isSpaceFree(board, move):
    # Checking for if place chosen is free
    return board[move] == ' '


def isBoardFull(board):
    # Making sure that every box has been filled with a letter
    for a in range(1, 10):
        if isSpaceFree(board, a):
            return False
    return True


def getPlayerMove(board):
    # Taking in players move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def isWinner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or  # across the top
            # across the middle
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            # across the bottom
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            # down the left side
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            # down the middle
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            # down the right side
            (board[9] == letter and board[6] == letter and board[3] == letter) or
            # diagonal
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[9] == letter and board[5] == letter and board[1] == letter))  # diagonal


def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard


def chooseRandomMoveFromList(board, movesList):
    # Checking for the right move made
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Taking the corner if not yet taken
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Taking the center if free
    if isSpaceFree(board, 5):
        return 5

    # Checking for a winning move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Making sure the player does not win
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Taking a side
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


print('Welcome to the game of Tic Tac Toe!')


while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        # this will be the players turn
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Congradulations! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('You have both tied in the game')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('You have lost to the computer!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('You have both tied in the game')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
