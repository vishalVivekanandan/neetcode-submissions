class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def dp(i):
            if memo[i] != -1:
                return memo[i]

            trail = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    trail = max(trail, 1 + dp(j)) # add 1 

            memo[i] = trail # for 
            return trail

        return max(dp(i) for i in range(n))
