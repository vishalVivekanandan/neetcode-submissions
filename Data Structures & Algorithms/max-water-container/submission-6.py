class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            # we cant get a better area keeping l, move it fwd
            if heights[l] <= heights[r]:
                l+=1
            # we cant get a better area keeping r, move it backwd
            else:
                r-=1
        return res


  
