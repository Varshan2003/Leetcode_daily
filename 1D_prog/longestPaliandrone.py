# class Solution:
#     def longestPalindrome(self, s):
#         if len(s)==1:return s
#         def isPaliandrome(s1):
#             return s1 == s1[::-1]
#         res=""
#         resLen = 0
#         for i in range(len(s)):
#             for j in range(len(s)):
#                 if isPaliandrome(s[i:j]) and len(s[i:j])>resLen:
#                     res = s[i:j]
#                     resLen = len(s[i:j])

#         return res

# s1 = Solution()
# print(s1.longestPalindrome("bb"))
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res