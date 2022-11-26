
class Node:
    def __init__(self, x, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        new_L = Node(0)
        temp1=new_L
        temp1=temp1.next
        temp = head
        while temp:
            temp1.val=temp.val
            temp1.next=temp.next
            temp1.random=temp.random
            temp1 = temp1.next
            temp = temp.next
        return [temp1.next.val,temp1.next.next,temp1.next.random]

s1  = Solution()
l1=Node(1)
l2 = Node(2)
l3 = Node(3)
l1.next = l2
l1.random = l3
print(s1.copyRandomList(l1))