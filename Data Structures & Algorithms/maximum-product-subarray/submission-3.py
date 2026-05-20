class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            prevMax, prevMin = curMax, curMin

            tmpMax = prevMax * num
            tmpMin = prevMin * num

            curMax = max(tmpMax, tmpMin, num)
            curMin = min(tmpMax, tmpMin, num)

            res = max(res, curMax, curMin)

        return res
