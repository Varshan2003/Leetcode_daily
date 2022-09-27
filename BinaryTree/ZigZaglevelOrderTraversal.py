# Definition for a binary tree node.
from collections import deque as queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def ZigZaglevelOrder(self, root):
        if not root:return []
        customqueue = queue()
        customqueue.append(root)
        ans = []
        j=0
        while customqueue:
            ans1=[]
            for i in range(len(customqueue)):
                root1 = customqueue.popleft()
                ans1.append(root1.val)
                if root1.left:
                    customqueue.append(root1.left)
                if root1.right:
                    customqueue.append(root1.right)
            if j%2!=0:
                ans.append(ans1[::-1])
            else:ans.append(ans1)
            j+=1
        return ans

T1 = TreeNode(3)
T2 = TreeNode(9)
T3 = TreeNode(20)
T4 = TreeNode(15)
T5 = TreeNode(17)
T1.left = T2
T1.right = T3
# T2.left = T4
# T2.right = T5
T3.left = T4
T3.right=T5
s1=Solution()
print(s1.ZigZaglevelOrder(T1))
        