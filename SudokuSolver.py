class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board=board
        self.solve()
    def rowCheck(self,row,num):
        for column in range(9):
            if self.board[row][column]==num:
                return False
        return True
    def colCheck(self,col,num):
        for row in range(9):
            if self.board[row][col]==num:
                return False
        return True
    def squareCheck(self,row,col,num):
        row=row-row%3
        col=col-col%3
        for i in range(row,row+3):
            for j in range(col,col+3):
                if self.board[i][j]==num:
                    return False
        return True
    def Valid(self,row,col,num):
        if self.rowCheck(row,num) and self.colCheck(col,num) and self.squareCheck(row,col,num):
            return True
        return False
    def empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j]==".":
                    return i,j
        return -1,-1
    def solve(self):
        row,col=self.empty()
        if row==-1 and col==-1:
            return True
        for i in range(1,10):
            if self.Valid(row,col,str(i)):
                self.board[row][col]=str(i)
                if self.solve():
                    return True
                
                self.board[row][col]="."
        return False