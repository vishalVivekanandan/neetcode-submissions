class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        stack = []

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        # for every closed bracket, if the last one isnt the open bracket of that, then return false
        
        # if you finish iterating through every el, the stack should be empty


        return True if not stack else False