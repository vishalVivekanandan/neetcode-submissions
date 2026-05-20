class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store = []
        # for i in nums:
        #     if target - i not in store:
        #         store.append(i)
        #     else:
        #         return [target-i, i]
        store = {}
        for i, j in enumerate(nums):
            if target - j in store:
                return [store[target - j], i]
            store[j] = i
