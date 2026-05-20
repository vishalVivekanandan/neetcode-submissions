class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in squares[r//3, c//3] or board[r][c] in rows[r] or board[r][c] in cols[c]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

# squares:
# {
#   (0, 0): {'1','2','3','4','5','6','7','8','9'},
#   (0, 1): {'1','2','3','4','5','6','7','8','9'},
#   (0, 2): {'1','2','3','4','5','6','7','8','9'},
#   (1, 0): {'1','2','3','4','5','6','7','8','9'},
#   (1, 1): {'1','2','3','4','5','6','7','8','9'},
#   (1, 2): {'1','2','3','4','5','6','7','8','9'},
#   (2, 0): {'1','2','3','4','5','6','7','8','9'},
#   (2, 1): {'1','2','3','4','5','6','7','8','9'},
#   (2, 2): {'1','2','3','4','5','6','7','8','9'},
# }
        return True


