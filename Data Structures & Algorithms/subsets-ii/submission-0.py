class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # maintain return array
        # output = []
        # sort nums
        # subset = []
        nums.sort()
        output = []
        subset = []

        def dfs(i):
            if i == len(nums):
                output.append(subset.copy())
                return
            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)

        dfs(0)
        return output 
