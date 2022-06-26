# 2. Вы когда-нибудь играли в игру "Крестики-нолики"?
# Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.
from functools import reduce

init_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def print_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print("{:4d}".format(board[row][col]), end="")
        print()


def tic_tac_toe_game():
    board = init_board
    turns_counter = 0
    flag = True

    while True:  

        turns_counter += 1

        while True:
            
            if turns_counter % 2:
                print(f'Turn: {turns_counter} for CROSS')
                flag = True
            else:
                print(f'Turn: {turns_counter} for ZERO')
                flag = False

            print('Enter a row:')
            row = input()
            print('Enter a col:')
            col = input()
            point = int(row), int(col)

            if board[point[0]][point[1]] == 0:
                board[point[0]][point[1]] = -1 if flag else 1
                if flag:
                    print(f'CROSS player signed {point}')
                else:
                    print(f'ZERO player signed {point}')
                break
            else:
                print(f'that cell already signed')

        print_board(board)

        # checks for win

        for i in range(3):  # verticals & horizontals, checks whether three crosses or zeroes in a row or a column
            sum1 = reduce(lambda x, y: x + y, [board[0][i], board[1][i], board[2][i]])
            sum2 = reduce(lambda x, y: x + y, [board[i][0], board[i][1], board[i][2]])
            if sum1 == 3 or sum2 == 3:
                print(f'ZERO player wins')
                return
            if sum1 == -3 or sum2 == -3:
                print(f'CROSS player wins')
                return

        d = [board[x][x] for x in range(3)]  # very naive diagonals checking

        main_diag_sum = board[0][0] + board[1][1] + board[2][2]
        aux_diag_sum = board[2][0] + board[1][1] + board[0][2]

        if main_diag_sum == 3 or aux_diag_sum == 3:
            print(f'ZERO player wins')
            break
        if main_diag_sum == -3 or aux_diag_sum == -3:
            print(f'CROSS player wins')
            break

        if turns_counter == 9:
            print('withdraw')
            break

    print('Game over')


tic_tac_toe_game()

