board = [
    [0,0,1,0,0,0,0,0,0],
    [3,6,0,0,8,0,0,0,7],
    [9,0,0,0,1,5,6,2,0],
    [0,8,3,0,9,7,2,4,5],
    [0,0,2,5,4,0,3,7,6],
    [5,0,0,0,0,0,0,9,0],
    [0,5,0,8,0,0,7,6,3],
    [7,0,6,4,0,0,0,0,0],
    [2,0,8,0,0,6,9,0,4]
]

def solve():

    find = find_empty()

    if not find:

        return True

    else: # find empty function returned a value indicating there is an  empty space

        row, col = find

    for i in range(1,10):

        if valid(i, (row, col)):

            board[row][col] = i
        
            if solve(): 

                return True

            board[row][col] = 0 # if number we just tested doesnt work remove from board then go back try again with a different value

    return False

def valid(num, pos):

    # row

    for i in range(len(board[0])):

        if board[pos[0]][i] == num and pos[1] != i:

            return False

    # column

    for i in range(len(board)):

        if board[i][pos[1]] == num and pos[0] != 1:

            return False

    # 3 x 30

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):

        for j in range(box_x * 3, box_x * 3 + 3):

            if board[i][j] == num and (i, j) != pos:

                return False

    return True

def print_board():

    for i in range(len(board)):
        
        if i % 3 == 0 and i != 0:

            print('- - - - - - - - - - - -') 

        for j in range(len(board[0])):

            if j % 3 == 0 and j != 0:

                print(' | ', end = '') 

            if j == 8:

                print(board[i][j]) 

            else:

                print(str(board[i][j]) + ' ', end = '')

def find_empty():

    for i in range(len(board)):

        for j in range(len(board[0])):

            if board[i][j] == 0:

                return (i, j) # row, column

    return None

print_board()
print('')
solve()
print('')
print_board()
            
