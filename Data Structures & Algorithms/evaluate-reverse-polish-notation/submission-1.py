class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        stack = []
        
        for num in tokens:
            if num == "+":
                two = stack.pop()
                one = stack.pop()
                stack.append(one+two)
            elif num == "-":
                two = stack.pop()
                one = stack.pop()
                stack.append(one-two)
            elif num == "*":
                two = stack.pop()
                one = stack.pop()
                stack.append(one*two)
            elif num == "/":
                two = stack.pop()
                one = stack.pop()
                stack.append(int(float(one)/two))
            else:
                stack.append(int(num))
        
        return stack[0]
            
            
