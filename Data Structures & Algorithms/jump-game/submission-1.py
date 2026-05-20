class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # see if we can work to the beginning from the end instead
        
        goal = len(nums) - 1
        
        # start at the last index, shift left once, end at the 1st index
        for i in range(len(nums) - 1, -1, -1):
            
            # can nums[i] take me to the goal element?
            if i + nums[i] >= goal: 
                # if so, i is the new goal post
                goal = i
        # if new goal is start, then we can go from start to end
        return goal == 0



