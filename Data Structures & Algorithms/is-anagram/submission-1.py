class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort, then compare?
        # time complexity: nlogn
        # space complexity: n
        # if same, return true, else return false

        # OR, use a hash table to store the frequency of each char in each string, then compare the two hash tables
            # if same, return true, else return false
        
        if len(s) != len(t):
            return False
            
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

            



