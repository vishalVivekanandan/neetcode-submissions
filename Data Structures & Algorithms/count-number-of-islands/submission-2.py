class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            # if its out of range or if its a 0, we've finished traversing the island
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                grid[r][c] == '0'):
                return 
            # mark the current location as a 0 bc we've visited it
            grid[r][c] = '0'
            
            # explore 4 directions to explore rest of island
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    # we use this to nuke an island (make all adjacent 1s 0s, exit if we see a 0)
                    dfs(r,c)
                    # once we nuke the island, increment count
                    count +=1
        return count
    