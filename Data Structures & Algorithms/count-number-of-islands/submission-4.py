class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count +=1
        return count
    # brute force approach:
        # loop through every element in grid
            # if element is 1
                # make elemnt 0 and explore element to top, bottom, left, and right of grid
                    # if element is 1:
                        # make 0 and explore l,r,t,b
                        # if element is 0:
                            # return
                
                # increment count
            # else, continue (no need for code here)
        # return count

