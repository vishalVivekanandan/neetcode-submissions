class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # final list
        
        # [0,1,2,...]
        
        subset = []

        def dfs(i):
            # if i is out of bounds, we return
            if i > len(nums) - 1:
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # decision to not include nums[i]
            subset.pop() # pop the one we just appended and run dfs without appending
            dfs(i+1)
        dfs(0)
        return  res

            
            


