class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = { ")":"(", "]":"[", "}":"{" }
        
        for c in s:
            # if the char is a closing one, the top one btter be the opening one
            if c in close_to_open:               
                if stack and close_to_open[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False