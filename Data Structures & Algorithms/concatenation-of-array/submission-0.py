class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # You are given an integer array nums of length n. 
        # Create an array ans of length 2n where 
            # ans[i] == nums[i] 
            # and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
        ans = []

        for _ in range(2):
            for num in nums:
                ans.append(num)
        
        return ans



        