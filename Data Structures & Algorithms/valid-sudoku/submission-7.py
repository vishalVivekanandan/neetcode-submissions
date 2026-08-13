class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Each row must contain the digits 1-9 without duplicates.
        def validRows(x):
            seen = set()
            for n in board[x]:
                if n == ".":
                    continue
                if n in seen:
                    return False
                else:
                    seen.add(n)
            return True

        # Each column must contain the digits 1-9 without duplicates.
        def validCols(y):
            seen = set()
            for x in range(9):
                if board[x][y] == ".":
                    continue
                if board[x][y] in seen:
                    return False
                else:
                    seen.add(board[x][y])
            return True
        
        # figure out the right grid based on x&y then check validity
        def validGrid(x, y):
            start_x, start_y = (x % 3) * 3, (y % 3) * 3
            seen = set()
            for x in range(start_x, start_x+3):
                for y in range(start_y, start_y+3):
                    if board[x][y] == ".":
                        continue
                    if board[x][y] in seen:
                        return False
                    seen.add(board[x][y])
            return True

        for x in range(len(board)):
            if not validRows(x):
                return False
            for y in range(len(board)):
                if not validCols(y):
                    return False
                if not validGrid(x, y):
                    return False
        return True
