from inspect import stack


# class MinStack:
#     def __init__(self):
#         self.minEls = 0
#         self.stack = []
        

#     def push(self, val):
#         self.stack.append(val)
        
             
#     def pop(self):
#         self.stack.pop()
        
#     def top(self):
#         return self.stack[-1]
        
#     def getMin(self):
#         return min(self.stack)

class MinStack:
    def __init__(self):
        self.minEls = 0
        self.stack = []
        

    def push(self, val):
        self.stack.append(val)
        
             
    def pop(self):
        self.stack.pop()
        
    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return min(self.stack)
        
s1 = MinStack()
s1.push(1)
s1.push(5)
s1.push(9)
s1.push(0)
s1.push(-1)
s1.push(-6)
print(s1.getMin())

