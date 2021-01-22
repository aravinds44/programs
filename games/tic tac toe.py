board = [' ' for x in range(10)]


def inputmove(letter, pos):
    board[pos] = letter


def printboard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def is_winner(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or \
            (board[4] == letter and board[5] == letter and board[6] == letter) or \
            (board[7] == letter and board[8] == letter and board[9] == letter) or \
            (board[1] == letter and board[4] == letter and board[7] == letter) or \
            (board[2] == letter and board[5] == letter and board[8] == letter) or \
            (board[3] == letter and board[6] == letter and board[9] == letter) or \
            (board[1] == letter and board[5] == letter and board[9] == letter) or \
            (board[3] == letter and board[5] == letter and board[7] == letter))


def player_move():
    run = True
    while run:
        move = int(input('Entre position to place X (1-9) : '))
        if move > 0 and move < 10:
            if free_space(move):
                run = False
                inputmove('X',move)
            else:
                print('This position is occupied !')
        else:
            print('Please type a number within the range')


def comp_move():
    place=0
    possible_moves=[]
    for x in range(1,10):
        if board[x]==' ':
            possible_moves.append(x)

    for play in ['O','X']:
        for i in possible_moves:
            board2=board[:]
            board2[i]=play
            if is_winner(board2,play):
                place=i
                return place
    free_corners=[]
    for i in possible_moves:
        if i in [1,3,7,9]:
            free_corners.append(i)
    if len(free_corners)>0:
        place=play_random(free_corners)
        return place

    free_edges = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            free_edges.append(i)
    if len(free_edges) > 0:
        place = play_random(free_edges)
    return place


def free_space(pos):
    if (board[pos] == ' '):
        return True
    else:
        return False


def board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def play_random(list):
    import random
    return random.choice(list)


print('Welcome to TicTacToe')
printboard(board)

while (not (board_full(board))):
    if not (is_winner(board, 'O')):
        player_move()
        printboard(board)
    else:
        print('O wins the game')
        break

    if not (is_winner(board, 'X')):
        move=comp_move()
        inputmove('O',move)
        print('Ai placed O in ',move)
        printboard(board)
    else:
        print('X wins the game')
        break
    if board_full(board):
        print("Match tie")
        break
