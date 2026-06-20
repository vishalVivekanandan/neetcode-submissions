class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        
        for i in range(n+1):
            # while we've reached the end or the current height is less than or eq to topmost stack
            # we will calculate area and re-assign if its larger
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i-stack[-1] -1
                maxArea = max(maxArea, height*width)
            
            stack.append(i)
        
        return maxArea