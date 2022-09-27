class Solution:
    def containsDuplicate(self, nums):
        nums1=set()
        for i in nums:
            if i in nums1:return True
            nums1.add(i)
        return False
    def containsDuplicate2(self, nums,k):
        nums1=[]
        for i in range(len(nums)):
            if nums[i] in nums1 and abs(nums1.index(nums[i])-i)<=k:
                return True
            nums1.append(nums[i])
        return False
        
    
s1 = Solution()
print(s1.containsDuplicate2([1,2,3,1,2,3],2))