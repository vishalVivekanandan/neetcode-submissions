class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash = {}
        for n in nums:
            if n not in hash:
                hash[n] = 1
            else:
                return n
        