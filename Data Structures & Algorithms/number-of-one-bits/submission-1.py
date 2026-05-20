class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # bitwise n and 1 (n&1) checks if least significant bit of n is 1
            if n & 1:
                res+=1
            # shift n one bit to the right
            n >>=1
        return res