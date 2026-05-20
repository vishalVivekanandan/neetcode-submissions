class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)): # ignore diagonal so do i+1
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

