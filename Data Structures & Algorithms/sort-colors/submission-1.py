class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we want to create 3 ptrs: l,i,r (boundry for 0, current element, boundry for 2)
        l,r = 0, len(nums) - 1
        i = 0
        
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        while i <= r:
            # we want 0 to be in the left so we swap with left and increment left and i
            if nums[i] == 0:
                swap(l, i)
                l += 1
                i += 1
            # we want 2 to be right so we swap with right and decrement r
            # we dont increment i as we want to check what i val is
            elif nums[i] == 2:
                swap(r, i)
                r -= 1
            # if it's 1, we move on
            else:
                i += 1
