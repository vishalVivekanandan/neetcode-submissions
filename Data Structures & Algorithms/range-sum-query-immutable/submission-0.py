class NumArray:

    def __init__(self, nums: List[int]):
        # creates prefix sum
        l = len(nums) + 1

        self.prefix = [0] * l
        for i in range(1, l):
            self.prefix[i] = self.prefix[i-1] + nums[i-1]
        

    def sumRange(self, left: int, right: int) -> int:
        # gives asnwer
        return self.prefix[right+1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)