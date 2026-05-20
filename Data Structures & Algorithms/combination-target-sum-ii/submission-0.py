class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        subset = []

        def dfs(start, curSum):
            if curSum == target:
                res.append(subset.copy())
                return
            if curSum > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                dfs(i+1, curSum + candidates[i])
                subset.pop()
        dfs(0,0)
        return res