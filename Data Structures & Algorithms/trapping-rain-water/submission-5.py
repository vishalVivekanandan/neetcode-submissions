class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        area = 0
        # i need to do a thing
        # i need to calculate the final area by calculating the amount of water trapped

        while l < r:
            if leftmax < rightmax:
                l +=1
                leftmax = max(leftmax, height[l])
                area += leftmax - height[l]
            else:
                r -=1
                rightmax = max(rightmax, height[r])
                area += rightmax - height[r]
        return area


