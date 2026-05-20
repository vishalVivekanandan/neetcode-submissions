class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []

        def dfs(depth):
            if depth > len(nums) - 1:
                res.append(subsets.copy())
                return
            subsets.append(nums[depth])
            dfs(depth+1)
            subsets.pop()
            dfs(depth+1)
        dfs(0)
        return res
            


