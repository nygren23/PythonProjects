
# hard coded board for now
sudokuBoard = [
    [9, 0, 0, 0, 1, 0, 0, 0, 2],
    [4, 1, 0, 0, 6, 3, 0, 0, 9],
    [0, 3, 2, 0, 0, 4, 6, 0, 0],
    [0, 0, 0, 3, 4, 0, 0, 0, 0],
    [0, 2, 8, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 2, 0, 0, 0, 0],
    [0, 8, 1, 0, 0, 5, 3, 0, 0],
    [2, 7, 0, 0, 3, 1, 0, 0, 5],
    [5, 0, 0, 0, 8, 0, 0, 0, 4]
    ]

# check whether the proposed number is playable
# in the specific square        
def canPlay(board, x, y, num):

    # check for num in same row (x)
    if num in board[x]:
        return False

    # check for num in same column (y)
    for i in range(9):
        if(board[i][y] == num):
            return False
    
    # check for num in same box
    boxX = x // 3
    boxY = y // 3

    for i in range(boxX * 3, boxX * 3 + 3):
        for j in range(boxY * 3, boxY * 3 + 3):
            if(board[i][j] == num):
                return False

    return True

# use backtracking to recursively solve the puzzle
def solve(board):
    
    for i in range(9):
        for j in range(9):

            if(board[i][j] == 0):
                for n in range(1, 10):
                    if(canPlay(board, i, j, n)):
                        board[i][j] = n
                        if(solve(board) == True):
                            return True
                        board[i][j] = 0
                return False
                
    return True
    
# print the sudoku board
def printBoard(board):
    for i in range(9):
        # end of box
        if(i % 3 == 0 and i != 0):
            print("----------------------")
        line = ""
        for j in range(9):
            if(j % 3 == 0 and j != 0):
                line += "| "
            line += str(board[i][j])
            if(j != 8):
                line += " "
        print(line)

def main():

    # print unsolved board
    printBoard(sudokuBoard)
    print("")

    # solve
    solve(sudokuBoard)

    print("**********************")
    print("*******SOLVED*********")
    print("**********************\n")

    # print solved
    printBoard(sudokuBoard)

if __name__ == '__main__':
    main()


