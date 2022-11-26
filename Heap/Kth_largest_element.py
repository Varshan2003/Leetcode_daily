import heapq
class Solution:
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)
        return nums[0]

s1=Solution()
print(s1.findKthLargest([3,2,3,1,2,4,5,5,6], k = 4))

        