class Solution:
    def encode(self, strs: List[str]) -> str:
        # strs = ["neet","code","love","you"]
        if not strs:
            return ""
        sizes, res = [], ""
        
        for s in strs:
            sizes.append(len(s))
        # list containing sizes of each word
        # sizes = [4,4,4,3]

        for sz in sizes:
            res += str(sz)
            res += ','
        # stringify the list
        # res = '4,4,4,3'
        res += '#'
        # res = '4,4,4,3#'

        for s in strs:
            res += s
        # res ='4,4,4,3#neetcodeloveyou"
        return res

    def decode(self, s: str) -> List[str]:
        # s ='4,4,4,3#neetcodeloveyou"
        if not s:
            return []

        sizes, res, i = [], [], 0

        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                # 4 then 4 then 4 then 3
                i += 1
                # increment i if its not a comma
            sizes.append(int(cur))
            i += 1
            # increment i even if its a comma
        i += 1
        # increment i if its a #

        # sizes = [4,4,4,3]
        # i=8

        # slice up s to put each word in it into res based on the sizes values and i index
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res



