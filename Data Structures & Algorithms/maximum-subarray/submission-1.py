class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            # holy shit this is genius
                # think - if it falls below 0, we have a guaranteed sol that is at least 0 in line 3
                
                # and if there's a MASSIVE value later on, we will still count it without prev vals
                # dragging down the curSum :)
                # simple yet works ;)
                
            if curSum < 0:
                curSum = 0
            
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub