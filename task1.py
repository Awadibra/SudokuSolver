import sys

# find an empty cell in the board, represented by number 0
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] == 0):
                return (i,j)
    return None

# check the cell if valid to fill with num
def valid(board, num, pos, root):
    # check row
    for i in range(len(board)):
        if (board[pos[0]][i] == num and pos[1] != i):
            return False
    # check column
    for i in range(len(board)):
        if(board[i][pos[1]] == num and pos[0] != i):
            return False
    # check surrounding box
    box_x = pos[1] // root
    box_y = pos[0] // root
    for i in range(box_y*root, box_y*root + root):
        for j in range(box_x*root, box_x*root + root):
            if(board[i][j] == num and (i,j) != pos):
                return False
    return True

# main backtracking loop
def solve(board, root):
    # find an empty cell to fill
    find = find_empty(board)
    # if none found, then we are done
    if not find:
        return True
    else:
        row, col = find
    # go over all cells and try to fill them recursively
    for i in range(1,root*root+1):
        if valid(board, i, (row,col), root):
            board[row][col] = i
            # this is where the backtracking happens
            if solve(board,root):
                # if found a solution we are done, otherwise backtrack
                return True
            # backtrack (by removing what we filled in the cell and returning to a previous one)
            board[row][col] = 0
    return False

# parse the given board and initialise cell values
def parse_board(lines):
    root = 0
    board = []
    for line in lines:
        line = line.split()
        # skip comments
        if line[0] == 'c':
            continue
        # grab root number and make the board
        elif line[0] == 'p':
            root = int(line[2])
            board = [[0 for x in range(root*root)]for y in range(root*root)]
        # fill the board with the initial cell values
        elif line [0] == 'v':
            board [int(line[2])-1][int(line[1])-1] = int(line[3])
    return (board,root)

# write the solution to the .sudoku.solution file for a single solution
def write_sol(sol_name, board):
    output = open("output\\"+sol_name, "w+")
    output.write("p sudoku "+ str(root)+"\n")
    for i in range(len(board)):
        for j in range(len(board)):
            output.write("v" + " " + str(j+1) + " " + str(i+1) + " " + str(board[i][j]) + "\n")

if __name__ == '__main__':
    arg = sys.argv[1]
    f = open(arg,"r")
    sol_name = arg.split("\\")
    sol_name = sol_name[-1] + ".solution"
    board,root = parse_board(f.readlines())
    print(board)
    solve(board,root)
    print(board)
    write_sol(sol_name, board)