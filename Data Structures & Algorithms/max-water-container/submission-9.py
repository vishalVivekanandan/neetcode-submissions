class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        # start pointers from sstart to end
        # move either one depending on the condition????
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(area, res)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res