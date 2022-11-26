class Solution:
    def subsetsWithDup(self, nums):
        res = []
        subset = []

        def dfs(i):
            if i >=len(nums):
                if ((subset.copy() not in res) and (subset.copy().reverse() not in res)):
                    res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

s1 = Solution()
print(s1.subsetsWithDup([1,2,2]))
