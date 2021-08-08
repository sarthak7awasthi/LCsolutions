class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        count=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    count+=1 
        return count

    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j]='0'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
        
#   another approach with dynamic programming(both are somewhat similar)

class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
  
        def area(r,c):
            
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]=="0":
                
                return 0
       
            grid[r][c]="0"
            
           
            return (1 +area(r+1, c)+ area(r-1, c)+area(r, c-1) + area(r, c+1))
        
        l=[area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0]))]

        counter=0
        for i in l:
            if i!=0:
                
                counter+=1
                
        
        return counter
