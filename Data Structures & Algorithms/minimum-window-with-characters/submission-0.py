class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        
        # freq of chars in t (populated in countT)
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # we need to take each char in string t and find them in s
        have, need = 0, len(countT)

        # we're trying to find min length so we assume its inf and work our way down
        res, resLen = [-1, -1], float("infinity")
        l = 0

        # iterate throuch each char in string s
        for r in range(len(s)):
            # char
            c = s[r]

            # in c window, we see this char one more time than before
            window[c] = 1 + window.get(c, 0)

            # we found a char that c is made up of and we have the right number of this specific car
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # if this is the case, we've found a window containing substring
            while have == need:
                # we found a new window that's smaller if this is true
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # we need to decrease count of this char bc we're "moving on from leftmost char"
                window[s[l]] -= 1
                # if we removed a char that was a part of the substring, we need to decrease count of have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # increment left ptr
                l += 1

        l, r = res # retrieve the indexes we've stored in res
        
        # print the substring using l and r; if resLen is inf there wasnt a substring at all
        return s[l : r + 1] if resLen != float("infinity") else ""

        



