class Solution:
    def validPalindrome(self, s):
        if s == s[::-1]:return True
        t=s
        for i in range(len(s)):
            p=t.replace(t[i],'')
            if p==p[::-1]:return True
            t=s
        return False

s1 = Solution()
print(s1.validPalindrome("deeee"))
