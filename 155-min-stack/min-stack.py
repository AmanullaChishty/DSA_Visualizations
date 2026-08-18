class MinStack:

    def __init__(self):
        self.main_stack=[]
        self.min_stack=[]
        

    def push(self, value: int) -> None:
        self.main_stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            min_val = min(value,self.min_stack[-1])
            self.min_stack.append(min_val)
        

    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.main_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()