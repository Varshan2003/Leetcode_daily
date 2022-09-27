class Solution:
    def twoSum(self, numbers,target):
        # for i in range(len(numbers)):
        #     for j in range(len(numbers)):
        #         if i==j:continue
        #         if numbers[i]+numbers[j]==target:return [i+1,j+1] 

        #---------TIME LIMIT EXCEEDED-----------
        l,r=0,len(numbers)-1
        while l < r:
            curr = numbers[l] + numbers[r]
            if curr > target:r-=1
            elif curr < target:l+=1
            else:return [l+1,r+1]


    
    

s1 = Solution()
print(s1.twoSum([-1,0],-1))
        