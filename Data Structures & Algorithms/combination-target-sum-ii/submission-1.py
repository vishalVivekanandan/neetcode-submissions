class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or i == len(candidates):
                return

            cur.append(candidates[i])
            # option 1: include candidates[i]
            dfs(i + 1, cur, total + candidates[i])
            
            # option 2: exclude candidates[i] AND
            # also exclude all duplicates of candidates[i]
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
        