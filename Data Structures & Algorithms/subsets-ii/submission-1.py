# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

#         nums.sort()
#         output = []
#         subset = []

#         def dfs(i):
#             if i == len(nums):
#                 output.append(subset.copy())
#                 return

#             subset.append(nums[i])
#             dfs(i + 1)
#             subset.pop()
        
#             while i + 1 < len(nums) and nums[i] == nums[i+1]:
#                 i+=1

#             dfs(i+1)

#         dfs(0)
#         return output 


# # O(n⋅2^n)
# # O(n)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        prev_Idx = idx = 0

        for i in range(len(nums)):
            idx = prev_idx if i >= 1 and nums[i] == nums[i - 1] else 0
            prev_idx = len(res)
            for j in range(idx, prev_idx):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)

        return res