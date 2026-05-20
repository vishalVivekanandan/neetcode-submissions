class Solution:
    def numDecodings(self, s: str) -> int:
        # given a string s, return the correct number of ways to decode it
        # empty string has 1 valid decoding
        memo = {len(s) : 1}
        # if 1-9: +1)
        # if 10-26: +2

        def dp(n):
            if n in memo:
                return memo[n]
            if s[n] == "0":
                return 0
            
            res = dp(n + 1)
            # if char is 10-26 and we're not out of bounds
                # in bound) n+1 < len(s)
                # 10-26) 1 or 2 and 0123456
            if n + 1 <= len(s)-1 and (s[n] == "1" or s[n] == "2" and s[n + 1] in "0123456"):
                res+= dp(n+2)
            memo[n] = res
            return res

        return dp(0)