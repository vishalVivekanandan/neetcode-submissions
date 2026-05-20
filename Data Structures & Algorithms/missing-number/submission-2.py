# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         xorr = n # max possible number
#         # xorr all numbers from 0-n with all numbers present in array, we'll be left with missing number
#         for i in range(n):
#             xorr ^= i ^ nums[i]
#         return xorr


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res
        # running sum:
        # for res = 4:
            # all is = 6
            # all nums[i] = all of i except 1 missing num
            # so i-nums[i] = missing num
