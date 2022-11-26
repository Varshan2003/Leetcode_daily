class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        if not head:return None
        length =0
        temp = head
        while temp:
            temp = temp.next
            length+=1
        if length==1:return None
        if length-n == 0 :return head.next
        temp1 = head
        for i in range(length-n-1):
            temp1 = temp1.next
        newN = temp1.next
        temp1.next = newN.next
        return head

n1 = ListNode(0)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(3)
n5 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

s1 = Solution()
print(s1.removeNthFromEnd(n1,2)) 