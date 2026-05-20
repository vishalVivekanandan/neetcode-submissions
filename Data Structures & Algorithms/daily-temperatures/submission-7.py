class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a stack to store pairs of temp, index for days that we havent found a warmer pair
        # iterate through whole temp list and while stack not empty AND temp is warmer than top of stack
            # compute how many days have passed and store that in the result 
        # otherwise, push current temp and index pair onto the stack

        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i-index
            stack.append((t, i))
        return res


        