class Solution:
    # def productExceptSelf(self, nums):
    #     ans=[]
    #     for i in range(len(nums)):
    #         temp=1
    #         for j in range(len(nums)):
    #             if i==j:continue
    #             temp = temp*nums[j]
    #         ans.append(temp)
    #     return ans ----------------------------------------------------O(n**2)class Solution:
    def productExceptSelf(self, nums):
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res #---------------------------------------------------------O(n)

s1 = Solution()
print(s1.productExceptSelf([0,0]))
        