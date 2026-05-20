class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break # we want sum to be 0, if smallest val is positive we cant find any more combinations
            if i > 0 and a == nums[i-1]: # whats the purpose of this?
                continue
            
            l, r = i+1, len(nums)-1 # start and end ptrs
            while l < r:
                sum = a + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # why do this:
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # skipping duplicates?
                        l += 1
        return res

            

            
        