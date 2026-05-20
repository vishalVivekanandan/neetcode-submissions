class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        
        pivot = l
        l, r = 0, len(nums) - 1
        
        # discard elements to the left of the pivot        
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot

        # discard the elements to the right of the pivot including the pivot el
        else:
            r = pivot - 1
        
        while l <=r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
                
