class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res





        # area = 0
        # iterate through start and nextStart initialized at start + 1:
            # if all vals to the right of start are less than start, break and return sum
            # if nextStart >= start, start = nextStart and nextStart += 1
            # if nextStart < start, add (start - nextStart) to area and increment nextStart
        




        