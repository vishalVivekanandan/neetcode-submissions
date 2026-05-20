class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # false by default except ending val
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # if we make it to the end its true

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                
                # w fits in remaining list and the length of the substring and w are the same
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)] # keep going down the tree
                
                if dp[i]: # break early because we reached to the end
                    break

        return dp[0]