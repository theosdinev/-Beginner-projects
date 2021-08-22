game_board = [
    [0,0,0,0,7,2,4,0,0],
    [6,0,0,8,3,1,0,0,0],
    [0,7,2,5,4,0,3,0,6],
    [0,4,7,9,2,8,0,6,0],
    [1,0,8,7,0,0,0,0,0],
    [9,0,0,0,1,0,8,0,0],
    [0,6,0,1,0,0,2,0,8],
    [0,3,5,0,8,4,6,0,0],
    [0,0,1,3,0,6,0,0,7]
     ]


def solver(bs):
    find = find_empty(bs)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1,10):
        if valid(bs, i, (row, column)):
            bs[row][column] = i

            if solver(bs):
                return True

            bs[row][column] = 0

    return False

def valid(bs, number, position):

    #checking through the row
    for i in range(len(bs[0])):
        if bs[position[0]][i] == number and position[1] != i:
            return False

    #checking the column
    for i in range(len(bs)):
        if bs[i][position[1]] == number and position[0] != i:
            return False

    #checking partition of puzzle
    partition_x = position[1] // 3
    partition_y = position[0] // 3

    for i in range(partition_y*3,partition_y*3 + 3):
        for j in range(partition_x*3, partition_x*3 + 3):
            if bs[i][j] == number and (i, j) != position:
                return False

    return True


def print_board(bs):

    for i in range(len(bs)):
        if i % 3 == 0 and i != 0:
            print("------------------------")

        for j in range(len(bs[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")


            if j == 8:
                print(bs[i][j])
            else:
                print(str(bs[i][j]) + " ", end="")

def find_empty(bs):
    for i in range(len(bs)):
        for j in range(len(bs[0])):
            if bs[i][j] == 0:
                return(i,j)   #first row then column

    return None






print_board(game_board)
solver(game_board)
print()
print()
print()
print_board(game_board)


