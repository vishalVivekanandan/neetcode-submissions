class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight
            ):
                return # if we already visited or out of bounds or went to smaller height
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS): # for every column
            # go through every single column in the 1st row (pacific)
            dfs(0, c, pac, heights[0][c]) 
            
            # go through every single column in last row (atlantic)
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) 

        for r in range(ROWS): # for every row
            dfs(r, 0, pac, heights[r][0]) # go through left most column (pacific)
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) # go through right most column (atlantic)


        # go through every coordinate and return ones that are in pacific and atlantic
        return [ [r, c] for (r, c) in (pac & atl) ]

     


