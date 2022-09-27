from collections import deque as queue
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def maxDepth(self, root):
        if not root:
            return
        customqueue = queue()
        customqueue.append(root)
        leftC = 0

        while customqueue:
            for i in range(len(customqueue)):
                root1 = customqueue.popleft()
                if root1.left:
                    customqueue.append(root1.left)
                if root1.right:
                    customqueue.append(root1.right)
            leftC+=1
        return leftC
    
    def maxDepth1(self, root):
        if not root:return 0
        return 1 + max(self.maxDepth1(root.left),self.maxDepth1(root.right))


T1 = TreeNode('Drinks')
T2 = TreeNode('coffee')
T3 = TreeNode('tea')
T4 = TreeNode('cold')
T5 = TreeNode('hot')
T1.left = T2

s1 = Solution()
print(s1.maxDepth1(T1))