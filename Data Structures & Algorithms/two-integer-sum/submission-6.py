class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index
        # values -> index
            # retrieve the index with the value 
        for i, v in enumerate(nums):
            diff = target - v
            if diff in indices:
                return [indices[diff], i]
            indices[v] = i