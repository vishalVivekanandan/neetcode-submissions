class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if the middle is less than the rightmost el, 
        # the min is in the left half including mid
        
        # otherwise the min is in the right half, excluding min

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
        