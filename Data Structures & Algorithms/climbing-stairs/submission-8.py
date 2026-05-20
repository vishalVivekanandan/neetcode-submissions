class Solution:
    def climbStairs(self, n: int) -> int:
        # you can choose 1 or 2
        # sum must equal n
        # how many distinct ways are there?
        cache = {}
        def dp(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in cache:
                return cache[n]
            
            cache[n] = dp(n-1) + dp(n-2)
            return cache[n]
        return dp(n)


 

