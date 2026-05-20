class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def backtrack(curSum, combList, i):
            if curSum > target or i >= len(nums):
                return
            if curSum == target:
                result.append(combList.copy())
                return
            
            combList.append(nums[i])
            backtrack(curSum + nums[i], combList, i)
            combList.pop()
            backtrack(curSum, combList, i+1)
            
    
        
        backtrack(0, [], 0)
        return result


     