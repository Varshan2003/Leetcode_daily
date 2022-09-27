from collections import deque as queue
def maxDepth(root):
    if not root:
        return
    customqueue = queue()
    customqueue.append(root)

    while customqueue:
        root1 = customqueue.popleft()
        print(root1.val)
        if root1.left:
            customqueue.append(root1.left)
        if root1.right:
            customqueue.append(root1.right)
        

