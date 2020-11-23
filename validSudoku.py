class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count=[0,1,2]  
        for k in range(0,3):
            if k==1:
                count=[3,4,5]
            elif k==2:
                count=[6,7,8]
            for row in board:
                if row==board[0] or row==board[3] or row==board[6]:
                    sq=[]

                i=0

                while i<len(count):

                    if row[count[i]]==".":
                        pass
                    elif row[count[i]] in sq:
                        return False
                    else:
                        sq.append(row[count[i]])
                    i+=1


        for row in board:
            C=[]
            for i in row:
                if i==".":
                    continue
                elif i in C:
                    return False
                else:
                    C.append(i)

        for i in range(0,9):
            d=[]
            for row in board:
                if row[i]==".":
                    pass
                elif row[i] in d:
                    return False
                else:
                    d.append(row[i])


        return True


                
                
                