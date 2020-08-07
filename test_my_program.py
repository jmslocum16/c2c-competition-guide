from importlib import import_module

program_name = 'basic_program.py'

module = import_module(program_name[:-3]) # remove .py from the end
module_run = getattr(module, 'run')

test_num = 0

def print_board(board):
    max_height = 6
    for x in range(max_height):
        j =  max_height - x - 1
        line = "|"
        for i in range(len(board)):
            if j < len(board[i]):
                line += board[i][j]
            else:
                line += " "
            line += "|"
        print(line)
    print("")

def do_test(board):
    global test_num

    print ('Test ' + str(test_num))
    test_num += 1

    print_board(board)
    move = module_run(board)

    print(program_name + ' played in column ' + str(move) + ':')

    if (move < 0 or move >= 7):
        print(str(move) + ' not a valid column!')
    elif (len(board[move]) >= 6):
        print('column ' + str(move) + ' is already full!')
    else:
        board[move].append('B')
        print_board(board)

    print('\r\n')

    

# test with empty
do_test([[], [], [], [], [], [], []])

# test with non-empty
do_test([['R', 'B'], ['R'], [], [], [], [], ['B']])

# test play to win
do_test([['R', 'B'], ['R'], [], [], ['B'], ['B'], ['B']])

# test play to not lose
do_test([['B', 'B'], ['B'], [], [], ['R'], ['R'], ['R']])

# test plays in a non-full column
do_test([['R', 'B', 'R', 'B', 'R', 'B'], ['R', 'B', 'R', 'B', 'R', 'B'], ['R', 'B', 'R', 'B', 'R', 'B'], ['B', 'R', 'B', 'R', 'B', 'R'], ['R', 'B', 'R', 'B', 'R', 'B'], ['R', 'B', 'R', 'B', 'R'], ['R', 'B', 'R', 'B', 'R', 'B']])

# TODO add my test cases here


