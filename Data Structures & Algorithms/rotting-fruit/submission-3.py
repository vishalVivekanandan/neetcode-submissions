class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        fresh = 0
        directions = [ [0,1], [0,-1], [1,0], [-1,0] ]

        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        
        while fresh > 0 and q:
            res += 1
            length = len(q)
            for _ in range(length):
                row, col = q.popleft()
                for dr, dc in directions:
                    if 0 <= row + dr < ROWS and 0 <= col + dc < COLS and grid[row + dr][col + dc] == 1:
                        grid[row + dr][col + dc] = 2
                        fresh -= 1
                        q.append((row + dr, col + dc))
        
        return res if fresh == 0 else -1
           