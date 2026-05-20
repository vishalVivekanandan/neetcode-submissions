class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(r,c):
            # out of bounds
            if 0 > r or 0 > c or r >= ROWS or c >= COLS:
                return
            
            # water
            if grid[r][c] == "0":
                return
            
            # now its water
            grid[r][c] = "0"

            # explore
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
        
        return count

