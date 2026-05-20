class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*len(nums)

        def dp(n):
            if n >= len(nums):
                return 0
            if cache[n] != -1:
                return cache[n]
            cache[n] = max(dp(n+1), nums[n]+dp(n+2))
            return cache[n]
        return dp(0)
            