import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        

    def add(self, val):
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

s1 = KthLargest(3,[4, 5, 8, 2])
print(s1.add(1))



        
