class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, rows * cols - 1

        while start <= end:
            m = (start+end) // 2
            r, c = m // cols, m % cols
            if target > matrix[r][c]:
                start = m+1
            elif target < matrix[r][c]:
                end = m-1
            else:
                return True
        return False

        