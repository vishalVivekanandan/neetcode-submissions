class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1        
        maxArea = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            maxArea = max(maxArea, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea


        # maxArea = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         diff = j-i
        #         area = min(heights[i], heights[j]) * diff
        #         maxArea = max(area, maxArea)
        # return maxArea



        