class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) > 0:
            if val <= self.minStack[-1]:
                self.minStack.append(val)
                self.minimum = val
        else:
            self.minStack.append(val)
            self.minimum = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minStack[-1]:  # also changed <= to == (cleaner)
            self.minStack.pop()
            self.minimum = self.minStack[-1] if self.minStack else float('inf')
            

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
