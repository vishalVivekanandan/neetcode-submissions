class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for ind, val in enumerate(nums):
            diff = target - val
            if diff in store:
                return [store[diff], ind]
            store[val] = ind
            
        