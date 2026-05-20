class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # see if we can work to the beginning from the end instead
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal: # is it possible for this jump take me to the max
                goal = i 
        return goal == 0