class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in s_set:
                s_set[s[i]] = 1
            if t[i] not in t_set:
                t_set[t[i]] = 1

            s_set[s[i]] = s_set[s[i]] + 1
            t_set[t[i]] = t_set[t[i]] + 1
        
        return s_set == t_set
        