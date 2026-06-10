class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i)- ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

        
        # res = defaultdict(list)

        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     res[tuple(count)].append(s)
        
        # return list(res.values())
        
        # the keys of the hash are the tuple representation of each word
        # the value is the string
        # so returning res.values returns the grouping of all strings that are anagrams

        # represent each string as a comparable val (hash)
        # instead, 
        # given a list of numbers how would you return the ones identical if you can only use comparator and not sort?

