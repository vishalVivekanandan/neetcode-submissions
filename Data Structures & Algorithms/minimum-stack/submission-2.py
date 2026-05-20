class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.minStack and self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        if self.stack: return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


 
        
