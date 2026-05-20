class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # this is Kadane's Algorithm.
        
        # keep track of max positive sum, reset if sum becomes negative
        # if it becomes negative, whats the point in carrying it over to the next block of vals?
        # return max sum

        maxSub, curSum = nums[0], 0

        for i in nums:
            if curSum < 0: # in case we end up with a negative number, cut trailing current sum off by resetting to 0
                curSum = 0
            curSum += i
            maxSub = max(maxSub, curSum) # keep track of non-negative max
        return maxSub

        