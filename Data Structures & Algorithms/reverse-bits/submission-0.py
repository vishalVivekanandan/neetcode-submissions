class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 #ith position of bit
            res += (bit << (31 - i)) # shift this bit to the last (relative to iteration) position
        return res