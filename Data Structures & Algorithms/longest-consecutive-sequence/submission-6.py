class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numSet = set(nums)
        # longest = 0

        # for num in numSet:
            
        #     # keep finding local minima, and compute the longest seq 
        #     if (num - 1) not in numSet:
        #         length = 1
        #         while (num + length) in numSet:
        #             length += 1
        #         longest = max(length, longest)
        
        # # this must be the lcs
        # return longest


        numset = set(nums)
        longest = 0

        for num in numset:
            if num-1 not in numset:
                length = 1
                while num+length in numset:
                    length +=1
                longest = max(longest, length)
        return longest