class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            diff = numbers[l] + numbers[r]
            if diff > target:
                r -= 1
            elif diff < target:
                l += 1
            else:
                # we're adding 1 bc they want 1-indexed positions
                return [l+1,r+1]
