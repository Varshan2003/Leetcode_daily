from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp = Counter(nums)
        ans = 0
        for value in mp.values():
            if value==1:
                return -1
            ans+=(value//3)
            if (value%3):
                ans+=1
        return ans
