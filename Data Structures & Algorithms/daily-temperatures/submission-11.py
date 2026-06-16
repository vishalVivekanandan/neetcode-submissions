class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stacktemp, stackind = stack.pop()
                res[stackind] = i - stackind
            stack.append((t, i))
        
        return res


        # i
        # 
        # t
        # 

        # temperatures=[30,38,30,36,35,40,28]


        # stack

            #



        # res
            # [1,0,0,0,0,0,0]

            # [1,4,1,2,1,0,0]