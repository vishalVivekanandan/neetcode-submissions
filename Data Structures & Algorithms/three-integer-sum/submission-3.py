class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for ind, val in enumerate(nums):
            if val > 0:
                break
            
            if ind > 0 and nums[ind] == nums[ind-1]:
                continue
            
            l = ind + 1
            r = len(nums) - 1
            
            while l < r:
                total = val + nums[l] + nums[r]
                if total > 0:
                    r -=1
                elif total < 0:
                    l +=1
                else:
                    results.append([nums[l], val, nums[r]])
                    l +=1
                    r -=1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1
                
            

        return results