class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        stack = []
        
        for num in tokens:
            if num == "+":
                # second = stack.pop()
                # first = stack.pop()
                stack.append(stack.pop()+stack.pop())
            elif num == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first-second)
            elif num == "*":
                # second = stack.pop()
                # first = stack.pop()
                stack.append(stack.pop()*stack.pop())
            elif num == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(float(first)/second))
            else:
                stack.append(int(num))
        
        return stack[0]
            
            
