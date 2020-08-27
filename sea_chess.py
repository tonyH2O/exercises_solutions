#!usr/bin/env python3

import math

def setup():

    global player1, player2
    player1_name = input('First Player to enter a name: ')
    player2_name = input('Second Player to enter a name: ')
    player1_sign = input("{} will you play with 'X' or will you choose 'O'?: ".format(player1_name)).lower()
    while player1_sign !='X'.lower() and player1_sign != 'O'.lower():
          player1_sign = input("{} will you play with 'X' or will you choose 'O'?: ".format(player1_name)).lower()

    player2_sign = 'X'.lower() if player1_sign == 'O'.lower() else 'O'.lower()
    player1 = [player1_name, player1_sign]
    player2 = [player2_name, player2_sign]

    print('This is the board numeration: ')
    print('|  1  |  2  |  3  |')
    print('|  4  |  5  |  6  |')
    print('|  7  |  8  |  9  |')
    print('First player opens the game!')



def draw_board(board):

    for x in board:
        print('|    ', end='')
        print('    |    '.join([str(y) for y in x]), end='')
        print('    |')


def check_if_won(current,board):

    global loop
    row1 = all([x == current[1] for x in board[0]])
    row2 = all([x == current[1] for x in board[1]])
    row3 = all([x == current[1] for x in board[2]])
    col1 = all([x == current[1] for x in [board[0][0], board [1][0], board[2][0]]])
    col2 = all([x == current[1] for x in [board[0][1], board [1][1], board[2][1]]])
    col3 = all([x == current[1] for x in [board[0][2], board [1][2], board[2][2]]])
    diagonal1 = all([x == current[1] for x in [board[0][0], board [1][1], board[2][2]]])
    diagonal2 = all([x == current[1] for x in [board[2][0], board [1][1], board[0][2]]])

    if any([row1,row2,row3,col1,col2,col3,diagonal1,diagonal2]):
        print('{} won!'.format(current[0]))
        loop = False


def check_if_tie():

    return not any(' ' in row for row in board)


def play(current,board):

    choice = input("{} choose a free position [1-9]: ".format(current[0]))
    
    while choice not in positions or board[positions[choice][0]][positions[choice][1]] != ' ':
        choice = input("{} choose a free position [1-9]: ".format(current[0]))

    row = math.ceil(int(choice) / 3) - 1
    col = int(choice) % 3 - 1
    board[row][col] = current[1]


    draw_board(board)
    check_if_won(current,board)
    check_if_tie()









player1 = None
player2 = None
board = [
        [' ',' ', ' '],\

        [' ',' ', ' '],\

        [' ',' ', ' ']
        ]

positions = {
        '1':[0,0],
        '2':[0,1],
        '3':[0,2],
        '4':[1,0],
        '5':[1,1],
        '6':[1,2],
        '7':[2,0],
        '8':[2,1],
        '9':[2,2]
        }
setup()
current = player1
other = player2
loop = True

while loop:
    play(current, board)
    current,other = other, current
    if check_if_won(current,board):
        break
    if check_if_tie():
        print('Tie!')
        break



