class Solution:
    def reverse(self, x: int) -> int:
        original = x
        x = abs(x)
        # num to string and reverse string and convert to int to remove trailing 0s
        res = int(str(x)[::-1]) 
        # if x was origianlly negative make res negative
        if original < 0:
            res *= -1
        # check if its between 32-bit range
        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0
        return res