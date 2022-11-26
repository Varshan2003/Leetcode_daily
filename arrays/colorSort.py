# class Solution:
#     def sortColors(self, nums):
#         for i in range(len(nums)-1):
#             for j in range(len(nums)-i-1):
#                 if nums[j]>nums[j+1]:
#                     nums[j],nums[j+1] = nums[j+1],nums[j]


# s1 =Solution()
# print(s1.sortColors([2,0,2,1,1,0]))

fh = open("varsh.txt","a")
for i in range(10):
    fh.write(str(i))

fh.close()
