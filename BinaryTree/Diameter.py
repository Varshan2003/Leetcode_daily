# from collections import deque as queue
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
# class Solution:
#     def maxDepth(self, root):
#         if not root:
#             return
#         customqueue = queue()
#         customqueue.append(root)
#         leftC = 0

#         while customqueue:
#             for i in range(len(customqueue)):
#                 root1 = customqueue.popleft()
#                 if root1.left:
#                     customqueue.append(root1.left)
#                 if root1.right:
#                     customqueue.append(root1.right)
#             leftC+=1
#         return leftC-1

#     def diameterOfBinaryTree(self,rootNode):
#         if not rootNode:return 0 
#         count1 = 0
#         count2 =0
#         if rootNode.left:
#             count1=1+self.maxDepth(rootNode.left)
#         if rootNode.right:
#             count2=1+self.maxDepth(rootNode.right)
#         return count1+count2

# T1 = TreeNode(1)
# T2 = TreeNode(2)
# T3 = TreeNode(3)
# T4 = TreeNode(4)
# T5 = TreeNode(5)
# T1.left = T2
# T1.right = T3
# T2.left = T4
# T2.right = T5

# s1 = Solution()
# print(s1.diameterOfBinaryTree())
class Solution:
    def diameterofBinaryTree1(self,root):
        res=0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res,left+right)
            return 1+max(left,right)
        dfs(root)
        return res

T1 = TreeNode(1)
T2 = TreeNode(2)
T3 = TreeNode(3)
T4 = TreeNode(4)
T5 = TreeNode(5)
T1.left = T2
T1.right = T3
T2.left = T4
T2.right = T5

s1 = Solution()
print(s1.diameterofBinaryTree1(T1))


