class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = []
        lenth = 1
        temp.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]>temp[-1]:
                temp.append(nums[i])
                lenth+=1
            else:
                ind = bisect_left(temp,nums[i])
                temp[ind] = nums[i]
        return lenth



