class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def sameTree(self,root1,root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1 and root2 and root1.val is root2.val:
            return self.sameTree(root1.left,root2.left) and self.sameTree(root1.right,root2.right)
    def isSubTree(self,p,s):
        if not s:return True
        if not p:return False
        if self.isSubTree(p,s):
            return True
        return self.isSubTree(p,s.left) or self.isSubTree(p,s.right)
        
T1 = TreeNode('Drinks')
T2 = TreeNode('coffee')
T3 = TreeNode('tea')
T4 = TreeNode('cold')
T5 = TreeNode('hot')
T1.left = T2
T1.right = T3
T2.left = T4
T2.right = T5
T3.right = T2
s1=Solution()
print(s1.isSubtree(T1,T4))