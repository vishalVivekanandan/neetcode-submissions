class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing, isDecreasing = True, True


        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                isIncreasing = False
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                isDecreasing = False

        return isIncreasing or isDecreasing
