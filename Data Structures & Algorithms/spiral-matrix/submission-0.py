class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # go top left to top right 
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # go top right to bottom right 
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            # there's a chance we stop here 
            if not (left < right and top < bottom):
                break
            
            # go bottom right to bottom left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # go bottom left to top left
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

            
        # once we break/end while loop we're done!
        return res