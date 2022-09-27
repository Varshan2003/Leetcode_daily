class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for strng in strs:
            current = sorted(strng)
            current = "".join(current)
            if current in dic:
                dic[current].append(strng)
                
            else:
                dic[current] = [strng]
                
        ans = []
        for string in dic:
            ans.append(dic[string])
            
        return ans

s1=Solution()

print(s1.groupAnagrams(["ana","naa","ada"]))


        
        