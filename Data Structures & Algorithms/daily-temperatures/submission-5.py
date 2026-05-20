class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, index = stack.pop()
                # index, temp = stack.pop()
                res[index] = i - index
            stack.append((t, i))
            # stack.append((i, t))

        return res
