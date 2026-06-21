class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # keep moving the window's left side right by one 
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # else add new el
            seen.add(s[r])
            res = max(res, r - l + 1)
        
        return res
