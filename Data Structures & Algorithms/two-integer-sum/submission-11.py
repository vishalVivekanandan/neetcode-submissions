class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for ind, val in enumerate(nums):
            goal = target - val
            if goal in seen:
                return [seen[goal], ind]
            
            seen[val] = ind
            
