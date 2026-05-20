class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visit = [False] * n
        perm = []
        nums.sort()
        
        def dfs():
            if len(perm) == n:
                res.append(perm.copy())
                return

            for i in range(n):
                if visit[i]: # skip if already visited
                    continue
                
                # skip if element equals previous one and it's visited
                if i and nums[i] == nums[i-1] and not visit[i-1]:
                    continue

                visit[i] = True
                perm.append(nums[i])
                dfs()
                visit[i] = False
                perm.pop()
        
        dfs()
        return res