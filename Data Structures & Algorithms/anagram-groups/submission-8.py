class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # i need to transform each word into a clear format which'll be keys of a hash - array counting freq
        # I need to then return the values for each key as a list and push said list into res

        # id just say use a hash as a key since ik how to do it and tc and sc is O(n), but is this allowed
        res = defaultdict(list)
        for s in strs:
            strrep = [0] * 26
            for c in s:
                strrep[ord(c) - ord("a")] += 1
            res[tuple(strrep)].append(s)
        return list(res.values())
            
            
                
