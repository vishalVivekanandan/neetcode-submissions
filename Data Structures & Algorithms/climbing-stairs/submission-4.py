class Solution:
    def climbStairs(self, n: int) -> int:
        # too inneficient (not an infinite loop)
        # def dfs(i):
        #     if i < n:
        #         return dfs(i+1) + dfs(i+2)
        #     if i == n:
        #         return 1
        #     return 0
        # return dfs(0)
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == n: return 1
            if i > n: return 0
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]

        return dfs(0)

