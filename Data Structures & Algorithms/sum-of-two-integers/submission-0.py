class Solution:
    def getSum(self, a: int, b: int) -> int:        
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF # largest possible 32-bit int

        while b != 0:
            carry = (a & b) << 1 # do we have a carry?
            a = (a ^ b) & mask # a xor b AND mask
            b = carry & mask # moves carry into b if it exists

        return a if a <= max_int else ~(a ^ mask)
        # if a overflows the unsigned 32-bit range, we have a negative number, 
        # convert it to a negative signed val