class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = nums[0] # 1st el of nums is 1st el of leftMax
        rightMax[n - 1] = nums[n - 1] # last el of nums is last el of rightMax

        for i in range(1, n):
            # we're out of the window
            if i % k == 0:
                leftMax[i] = nums[i] 
            # compare max with current num
            else:
                leftMax[i] = max(leftMax[i - 1], nums[i]) 
            
            # we're out of the window
            if (n - 1 - i) % k == 0:
                rightMax[n - 1 - i] = nums[n - 1 - i]
            
            # compare max with current num
            else:
                rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - 1 - i])
        # length based on window
        output = [0] * (n - k + 1)
        # print(leftMax)
        # print(rightMax)
        
        # compute max for window based on leftmax and rightmax
        for i in range(n - k + 1):
            output[i] = max(leftMax[i + k - 1], rightMax[i])
        
        # return
        return output