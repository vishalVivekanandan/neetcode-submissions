class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefix[0] = 1
        

        suffix = [0] * len(nums)
        suffix[len(nums)-1] = 1
        
        for n in range(1, len(nums)):
            prefix[n] = prefix[n-1] * nums[n-1]
        
        for j in range(len(nums)-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]

        # res = []
        res = [0] * len(nums)

        for k in range(len(nums)):
            res[k] = prefix[k] * suffix[k]
        return res


        
