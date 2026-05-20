class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIsland = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxIsland = max(maxIsland, dfs(r, c))

        return maxIsland

        