class Solution:
    def hasCycle(self, head):
        self.head = head
        if not self.head:
            return self.head
        if not self.head.next:return False
        if self.head == self.head.next:
            return True
        self.temp = []
        while self.head:
            if self.head in self.temp:
                return True
            self.temp.append(self.head)
            self.head = self.head.next
        return False