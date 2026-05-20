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


        # i want to keep track of a maximum count
            # this value can change as we encounter a 1 in an island so we need to change its value depending on when we see a 1
            # if we see a 1, mark it as 0 and increment count
            # then explore the top, bottom, left, and right while passing in current count
        # when we explore a new value, re-assign maxCount if applicable and return it once we iterate through everything


        # i should use a set to keep track of visited nodes

