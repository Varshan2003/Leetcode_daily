class Solution:
    def climbStairs(self, n):
        if n<=2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs2(self,n):
        first,second = 1,1
        for i in range(n-1):
            temp = first
            first = first+second
            second = temp
        return first

s1 = Solution()
print(s1.climbStairs2(3))
        