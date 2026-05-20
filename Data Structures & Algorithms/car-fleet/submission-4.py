class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p,s in pair:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


        # pair = [(p, s) for p, s in zip(position, speed)]
        # pair.sort(reverse=True)
        # stack = []

        # for p, s in pair:
        #     stack.append((target-p)/s) # time it takes to reach the target
        #     if len(stack) >= 2 and stack[-1] <= stack[-2]: # this means a further car surpassed position, pop it
        #         stack.pop()
        # return len(stack)

        # pair = [(p,s) for p, s in zip(position, speed)]
        # pair.sort(reverse=True)
        # stack=[]
        # for p,s in pair:
        #     stack.append((target-p)/s)
        #     if len(stack) >= 2  and stack[-1] <= stack[-2]:
        #         stack.pop()
        # return len(stack)



        

