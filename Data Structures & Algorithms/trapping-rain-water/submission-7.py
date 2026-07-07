class Solution:
    def trap(self, height: List[int]) -> int:
        
        # if the left wall is shorter, the right wall cant help us so we move left ptr inward
        # vice versa
        # as we move ptrs, we keep track of highest wall seen on each side, the water at each position is max wall on that side - height at that position
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
