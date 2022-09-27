
#------****SUCCESSFULL, WITHIN 15 MINUTES FIRST ALGORITHM****-------

class Solution:
    def longestConsecutive(self, nums):
        if not nums:return 0
        nums = sorted(nums)
        count1=1
        count=1
        for i in range(len(nums)-1):
            if (nums[i] == nums[i+1]):continue
            if (nums[i]+1 == nums[i+1]):
                count1+=1
                count = max(count1,count)
            else:
                count1 = 1
        return count                       

s1 = Solution()
print(s1.longestConsecutive([1,2,0,1,2,3,4,5]))

        