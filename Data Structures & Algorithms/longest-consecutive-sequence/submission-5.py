class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in numSet:
                count = 0
                while i in numSet:
                    count += 1
                    i += 1
                longest = max(count, longest) 
        return longest
        





            


