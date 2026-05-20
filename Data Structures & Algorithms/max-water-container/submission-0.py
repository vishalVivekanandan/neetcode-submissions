class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                diff = j-i
                area = min(heights[i], heights[j]) * diff
                maxArea = max(area, maxArea)
        return maxArea



        