class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        map1={}
        map2={}
        for i in range(len(s)):
            if s[i] not in t:
                return False
            if s[i] in map1:
                map1[s[i]]+=1
            else:
                map1[s[i]]=1
        for j in range(len(t)):
            if t[j] in map2:
                map2[t[j]]+=1
            else:
                map2[t[j]]=1
        o=[]
        for k in s:
            if k not in o:
                o.append(k)
        for z in o:
            if map1[z]!=map2[z]:
                return False
        return True


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


s = Solution()
print(s.isAnagram2("anagram","nagaram"))

        