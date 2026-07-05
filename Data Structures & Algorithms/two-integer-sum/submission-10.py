class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # construct a hash set in real time:
            # key = num, val = index
        # for each val, calculate the diff:
        # if the diff is in the hashmap, we found a sol
        # otherwise, put the num in the hashmap

        seen = {} 
        for ind, val in enumerate(nums):
            dif = target - val
            if dif in seen:
                return [seen[dif], ind]
            
            seen[val] = ind
        return 0