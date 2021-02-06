
    
def valid(board,row,col,n):
    curRow=row
    while curRow>=0:
        if board[curRow][col]=='Q':
            return False
        curRow-=1
    curRow=row
    curCol=col
    while curRow>=0 and curCol>=0:
        if board[curRow][curCol]=='Q':
            return False
        curRow=curRow-1
        curCol=curCol-1
    curRow=row
    curCol=col
    while curRow>=0 and curCol<n:
        if board[curRow][curCol]=='Q':
            return False
        curRow=curRow-1
        curCol=curCol+1
    return True

def backtrack(board,row,n):
    
    if row==n:
        print(board)
        return None
    for i in range(n):
        if valid(board,row,i,n):
            board[row][i]='Q'
            backtrack(board,row+1,n)
        board[row][i]='.'
def solveNQueens(n):
    board = [['.' for x in range(n)] for y in range(n)]
    backtrack(board,0,n)

    