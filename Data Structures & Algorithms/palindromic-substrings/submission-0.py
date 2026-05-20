class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.palindrome(s,i,i)
            res += self.palindrome(s,i,i+1)
        return res

    def palindrome(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res +=1
            l-=1
            r+=1
        return res
        









#         # resIdx = 0
#         # resLen = 0
#         res = 0

#         for i in range(len(s)):
            
#             l, r = i, i
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 # if (r - l + 1) > resLen: # longer palindrome
#                 #     resIdx = l #new left bound
#                 #     resLen = r - l + 1 # new rightbound
#                 res +=1
#                 l-=1
#                 r+=1

#             l,r = i,i+1
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 res +=1
#                 # if (r - l + 1) > resLen:
#                 #     resIdx = l
#                 #     resLen = r - l + 1
#                 l-=1
#                 r+=1
            
#         # return s[resIdx : resIdx + resLen]
#         return res



