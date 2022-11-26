class Solution:
    def lengthOfLastWord(self, s):
        p = s.split(" ")
        q=[]
        for i in p:
            if i!="":
                q.append(i)

        return len(q[-1])