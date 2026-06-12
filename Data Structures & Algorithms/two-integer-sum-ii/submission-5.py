class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # it takes O(n) to point to largest number that is less than target (r)
        l,r = 0, len(numbers) - 1
        
        while l < r:
            if numbers[r] + numbers[l] > target:
                r -= 1
            elif numbers[r] + numbers[l] < target:
                l += 1
            else:
                return [l+1, r+1]
        return []