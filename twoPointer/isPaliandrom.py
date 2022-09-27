class Solution:
    def isPalindrome(self, s):
        if s=="":return True
        s = s.lower()
        new_s=""
        for i in s:
            if (ord(i) in range(97,123)) or (ord(i) in range(48,58)):
                new_s+=i

        return new_s==new_s[::-1]

s1 = Solution()
print(s1.isPalindrome("`l;`` 1o1 ??;l`"))
        