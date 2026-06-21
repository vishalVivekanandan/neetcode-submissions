class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):

            count[s[r]] = 1 + count.get(s[r], 0)
            
            # max count of most appearing num
            maxf = max(maxf, count[s[r]])
            
            # move left part of window until condition holds
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            # recompute the max window
            res = max(res, r - l + 1)

        return res


