class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hash storing numbers as keys, and index as value
        # then go through each val in list with enum
            # calculate diff, if it's in hash and current index is diff from hash index of diff, return list
        # otherwise, return empty list

        indices = {} 

        for i, n in enumerate(nums): # index, number
            indices[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []


