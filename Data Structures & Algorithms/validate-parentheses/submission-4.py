class Solution:
    def isValid(self, s: str) -> bool:

        in_out = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []
        for c in s:
            if c in in_out:
                if stack and stack[-1] == in_out[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

        # ultimately, if we see a closing bracket, we have to see if the opening breacket is the last el
        # if so, we pop, otherwise we return false
        
        # push opening brackets to stack

        # if the stack is not empty at the end, we've failed

        