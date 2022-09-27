class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def HeightOfTree(self,root):
        if not root:return 0
        return 1+max(self.HeightOfTree(root.left),self.HeightOfTree(root.right))

    def isBalanced(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:return False

        if root1.val == root2.val:
            return self.isBalanced(root1.left,root2.left) and self.isBalanced(root1.right,root2.right)

T1 = TreeNode('Drinks')
T2 = TreeNode('coffee')
T3 = TreeNode('tea')
T4 = TreeNode('cold')
T5 = TreeNode('hot')
T1.left = T2
T1.right = T3
T2.left = T4
T2.right = T5

l1 = TreeNode('Drinks')
l2 = TreeNode('coffee')
l3 = TreeNode('tea')
l4 = TreeNode('cold')
l5 = TreeNode('hot')
l1.left = l2
l1.right = l3
l2.left = l4
l2.right = l5
S1 = Solution()
print(S1.isBalanced(T1,l1))