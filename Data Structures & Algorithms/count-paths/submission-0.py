class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for i in range(m)]

        def memoize(r,c,rows,cols):
            if r == rows or c == cols:
                return 0
            if r == rows-1 and c == cols-1:
                return 1
            if memo[r][c] != -1:
                return memo[r][c]
            memo[r][c] = memoize(r+1,c,rows,cols) + memoize(r,c+1,rows,cols)
            return memo[r][c]
        
        return memoize(0,0,m,n)




        


        