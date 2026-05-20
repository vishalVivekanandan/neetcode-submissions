class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in numSet:
                count = 1
                while i + count in numSet:
                    count += 1
                longest = max(longest, count)
        return longest

        # numSet = set(nums)

        # longest = 0

        # for i in nums:
        #     if i-1 not in numSet:
        #         count = 1
        #         while i + count in numSet:
        #             count += 1
        #         longest = max(longest, count)

        # return longest 
            


