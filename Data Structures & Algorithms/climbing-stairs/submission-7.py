class Solution:
    def climbStairs(self, n: int) -> int:
        
        # memo = {}
        # # can take away 1 or 2
        #     # if you reach the end return 1
        #     # if you exceed the end return 0
        # def dfs(n):
        #     if n == 0:
        #         return 1
        #     if n < 0:
        #         return 0
        #     if n in memo:
        #         return memo[n]
        #     memo[n]  = dfs(n-1) + dfs(n-2)
        #     return memo[n]
        # return dfs(n)

        # you can only climb stairs from 1 or 2 
            # so the total way to reach step i is the sum or ways to reach the previous steps
        one, two = 1, 1  
        for i in range(n - 1):
            one, two = two, one + two
        return two


