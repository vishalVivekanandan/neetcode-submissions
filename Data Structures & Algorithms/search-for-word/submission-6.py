# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:

#         ROWS, COLS = len(board), len(board[0])

#         def dfs(r, c, i):
#             if i == len(word):
#                 return True
            
#             # if out of bounds or unequal word or visited, return false
#             if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or board[r][c] == "#":
#                 return False
#             # mark as visited - backtrack
#             board[r][c] = "#"
            
#             # make 4 dfs calls
#             return dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            
#             # mark as unvisited - backtrack
#             board[r][c] = word[i]

        


#         for r in range(ROWS):
#             for c in range(COLS):
#                 if dfs(r, c, 0):
#                     return True
#         return False
            





class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            # if out of range, not equal char, or already visited
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False
            # mark

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            # backtrack
            board[r][c] = word[i]
            
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

        