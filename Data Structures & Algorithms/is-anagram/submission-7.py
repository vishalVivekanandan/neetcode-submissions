class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        for c in s:
            hash_s[c] = 1 + hash_s.get(c, 0)
        for c in t:
            hash_t[c] = 1 + hash_t.get(c, 0)
        return hash_t == hash_s
            