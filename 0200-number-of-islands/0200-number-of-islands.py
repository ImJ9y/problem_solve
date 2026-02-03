class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        num_island = 0

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != "1":
                return
            
            grid[r][c] = "0"
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] != "0":
                    dfs(i,j)
                    num_island += 1
        
        return num_island
        

