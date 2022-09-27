from collections import deque as queue
import bfs 
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def InvertTree(self,root):
        if not root:return 0
        if root.left or root.right:
            root.left,root.right = root.right , root.left
        self.InvertTree(root.left)
        self.InvertTree(root.right)
        return root.val
        

T1 = TreeNode('Drinks')
T2 = TreeNode('coffee')
T3 = TreeNode('tea')
T4 = TreeNode('cold')
T5 = TreeNode('hot')
T1.left = T2
T1.right = T3
T2.left = T4
T2.right = T5
s1 = Solution()
bfs.maxDepth(T1)
print("------")
s1.InvertTree(T1)
bfs.maxDepth(T1)