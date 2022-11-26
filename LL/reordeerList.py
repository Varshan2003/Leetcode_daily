from multiprocessing import dummy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        length = 0
        list = head
        while head:
            head = head.next
            length+=1
        dummy = ListNode()
        tail = dummy
        for i in range(length):
            list1 = list
            for j in range(length-i):
                list1 = list1.next
            if (i%2==0):
                tail.next = list1
            else:
                tail.next = list1.next
            tail = tail.next
        return [dummy.val , dummy.next.val , dummy.next.next.val , dummy.next.next.next.val]
                


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
print(s1.reorderList(n1))