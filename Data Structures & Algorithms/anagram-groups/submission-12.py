class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            rep = [0] * 26
            for c in s:
                rep[ord(c) - ord("a")] += 1
            
            seen[tuple(rep)].append(s)

        return list(seen.values())

