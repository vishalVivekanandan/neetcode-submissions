class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, comb):
            if i > n: # height of decision tree is n
                if len(comb) == k: # we may have combinations that are smaller or larger
                    res.append(comb.copy())
                return
            comb.append(i)
            backtrack(i+1, comb)
            comb.pop()
            backtrack(i+1, comb)
        backtrack(1, [])
        return res
