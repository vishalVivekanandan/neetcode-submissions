class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hash that contains list as key
        res = defaultdict(list)

        # create a list
        for s in strs:
            rep = [0] * 26
            for c in s:
                rep[ord(c)-ord("a")] += 1

            res[tuple(rep)].append(s)
        return list(res.values())
            

            