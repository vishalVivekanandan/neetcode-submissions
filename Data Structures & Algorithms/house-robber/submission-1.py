class Solution:
    def rob(self, nums: List[int]) -> int:
        # each el in nums represents money a house has
        
        # cannot take money from adj houses
            # what's the max money you can take

        # either take and skip
        # or just skip
        # total = 0
        #     take_now = 
        #     take_later = total
        #     total = max(take, skip)
        # i = 0
        # total = 0
        # while i <= len(nums) - 1:
        #     total += nums[i]
        #     i++

        # def take(n):
        #     if n > len(nums) - 1:
        #         return 0
        #     total +=
        cache = [-1]*len(nums)
        def take(i):
            if i > len(nums) - 1:
                return 0
            if cache[i] != -1:
                return cache[i]

            cache[i] = max(take(i + 1), nums[i] + take(i + 2))
            return cache[i]

        return take(0)



