class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n
        
        pref[0] = suff[n-1] = 1

        # 1,2,3,4
        # 1,1,2,6
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]
        
        # 1,2,3,4
        # 24,12,4,1
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        
        # 1,2,3,4
        # 1,1,2,6
        # 24,12,4,1
        # 24,12,8,6
        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res
