class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(start, curSum):
            if curSum == target:
                res.append(subset.copy())
                return
            if curSum > target:
                return
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                dfs(i, curSum + nums[i])
                subset.pop()
        dfs(0,0)
        return res
        

    