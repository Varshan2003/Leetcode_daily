#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def isValidBST(self, root):
        # if not root:return True
        # if root.left or root.right:
        #     left,right = True,True
        #     if root.left:
        #         if root.left.val < root.val:
        #             left= True
        #         else:left = False
        #     if root.right:
        #         if root.right.val >root.val:
        #             right = True
        #         else:return False
        #     return left and right
                
        # return self.isValidBST(root.left) and self.isValidBST(root.right)
class Solution:
    def isValidBST(self, root):
        def valid(node,left,right):
            if not node:return True
            if not(node.val > left and node.val<right):
                return False
            return valid(node.left,left,node.val) and valid(node.right,node.val ,right)
        return valid(root,float("-inf") ,float("inf"))
        
        
T1 = TreeNode(3)
T2 = TreeNode(2)
T3 = TreeNode(4)
T4 = TreeNode(1)
T5 = TreeNode(5)
T1.left = T2
T1.right = T3
T2.left = T4
T2.right = T5
s1 = Solution()
print(s1.isValidBST(T1))