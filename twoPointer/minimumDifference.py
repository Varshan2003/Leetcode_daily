class Solution:
    def minimumDifference(self, nums, k):
        if k==1:return 0
        nums.sort()
        nums.reverse()
        fin =[]
        l=-1
        for i in range(len(nums)):
            l+=1
            r = l+k-1
            if ((l <len(nums )) and (r < len(nums))):
                fin.append(nums[l]-nums[r])
        return min(fin)

s1 = Solution()
print(s1.minimumDifference([9,4,1,7], k = 2))
