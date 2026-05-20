class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1]*len(nums)

        def take(n):
            if n > len(nums) - 1:
                return 0
            if memo[n] != -1:
                return memo[n]
            memo[n] = max(nums[n] + take(n + 2), take(n+1))
            return memo[n]

        return take(0)



