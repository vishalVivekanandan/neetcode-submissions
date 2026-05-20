class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [[-1] * len(nums) for _ in range(2)]  # memo[flag][n]

        if len(nums) == 1:
            return nums[0]
        
        def take(n, flag):
            f = 1 if flag else 0
            
            if n > len(nums) - 1:
                return 0
            # we cant take the last one bc we took the 1st one
            if flag and n == len(nums) - 1: 
                return 0

             # we can take the last one bc we didnt take the 1st one
            if not flag and n == len(nums) - 1:
                return nums[n]
            # its in the cache
            if memo[f][n] != -1:
                return memo[f][n]


            memo[f][n] = max(take(n + 1, flag), nums[n] + take(n + 2, flag))
            return memo[f][n]

        return max( take(0, True), take(1, False) )

