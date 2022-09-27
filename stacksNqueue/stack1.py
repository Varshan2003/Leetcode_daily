class MinStack:
    def __init__(self):
        self.stack = []
        

    def push(self, val) :
        self.stack.append(val)
        
        

    def pop(self):
        self.stack.pop()
        

    def top(self):
        return self.stack[-1]

    def getMin(self):
        self.stack.sort()
        return self.stack[0]

Stack = MinStack()
Stack.push(3)
Stack.push(1)
Stack.push(9)
Stack.push(0)
Stack.push(4)
Stack.push(5)
Stack.pop()
print(Stack.getMin())
