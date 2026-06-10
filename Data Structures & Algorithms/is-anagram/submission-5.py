class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # create 2 hashes
        s_count = {}
        t_count = {}

        # populate them, then return equality
        for i in s:
            if i not in s_count:
                s_count[i] = 1
            s_count[i] += 1
        
        for j in t:
            if j not in t_count:
                t_count[j] = 1
            t_count[j] += 1
        
        return s_count == t_count