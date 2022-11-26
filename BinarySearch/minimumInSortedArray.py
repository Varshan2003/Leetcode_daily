class Solution:
    def findMin(self, nums):
        l,r = 0 , len(nums)-1
        if nums[l] <= nums[r]:
            return nums[l]
        while nums[r] > nums[r-1]:
            r-=1
        return nums[r]

s1 = Solution()
print(s1.findMin([0,1,2]))