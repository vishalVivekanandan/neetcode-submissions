class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        
        for ind, val in enumerate(nums):
            if nums[ind] > 0:
                break
            
            if ind > 0 and nums[ind - 1] == val:
                continue
            
            left = ind + 1
            right = len(nums) - 1
            
            while left < right:
                total = val + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left +=1
                else:
                    results.append([nums[left], val, nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left -1]:
                        left +=1

        
        return results

       
