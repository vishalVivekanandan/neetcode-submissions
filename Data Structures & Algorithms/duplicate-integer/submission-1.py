class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # put every single element of the array in a hash: O(n) time
        # check if the hash contains each element: O(n) for n elements
            # if true, return true
        # return false

        # Slightly different, this is a Hash Set (idk why it's not called just a set???)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        
        # # OR, just make a set out of the array, and if the length of it is less than the length of the array, return true else return false:
        # return len(set(nums)) < len(nums)

    
         