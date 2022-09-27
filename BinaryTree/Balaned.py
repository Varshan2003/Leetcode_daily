class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def HeightOfTree(self,root):
        if not root:return -1
        return 1+max(self.HeightOfTree(root.left),self.HeightOfTree(root.right))
    def isBalanced(self,root):
        if not root:return True
        if abs(self.HeightOfTree(root.left)-self.HeightOfTree(root.right))>1:
            return False
        left=self.isBalanced(root.left)
        right=self.isBalanced(root.right)
        return left&right

T1 = TreeNode(1)
T2 = TreeNode(2)
T3 = TreeNode(3)
T4 = TreeNode(4)
T5 = TreeNode(5)
T1.left = T2
# T1.right = T3
T2.left = T4
T2.right = T5
s1=Solution()
print(s1.isBalanced(T1))


        