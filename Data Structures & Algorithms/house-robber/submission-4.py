class Solution:
    def rob(self, nums: List[int]) -> int:
        #greedy!!!
        # for house i, we can either not rob it (i - 1)
        # or rob it (i + (i-2))
            # choose the better of 2 at each step
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[-1]

            