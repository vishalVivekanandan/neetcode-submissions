class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:        
        visited = set()
        def dfs(r, c):
            if (r == ROWS or c == COLS or r < 0 or c < 0 or grid[r][c] == 0 or (r, c) in visited):
                return 0
            visited.add((r, c))
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c-1) + dfs(r, c+1)
        
        maxCount = 0
        ROWS, COLS, = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                curCount = dfs(r, c)
                maxCount = max(maxCount, curCount)
        return maxCount
