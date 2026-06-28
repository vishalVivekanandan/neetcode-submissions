class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count, t_count = {}, {}
        
        if len(s) != len(t):
            return False

        for c in s:
            s_count[c] = 1 + s_count.get(c, 0)
        
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        return s_count == t_count

