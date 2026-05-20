class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1:
            return -1
        
        if grid[ROWS - 1][COLS - 1] == 1:
            return -1
        
        length = 1 
        
        directions = [
            [1, 0], [-1, 0], [0, 1], [0, -1],
            [1, 1], [1, -1], [-1, 1], [-1, -1]
        ]


        visit = set()
        queue = deque()

        queue.append((0, 0))
        visit.add((0, 0))
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                        continue
                    if (nr, nc) in visit:
                        continue
                    if grid[nr][nc] == 1:
                        continue

                    queue.append((nr, nc))
                    visit.add((nr, nc))

            length += 1
        
        return -1

