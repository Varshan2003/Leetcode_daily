class Solution:
    def inorderTraversal(self, root):
        res=[]
        def dfs(root):
            if not root:return 
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res