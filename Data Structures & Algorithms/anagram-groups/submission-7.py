class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            comp = [0] * 26
            for c in s:
                comp[ord(c)-ord("a")]+=1
            res[tuple(comp)].append(s)
        return list(res.values())
        