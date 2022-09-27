class Solution:
    def plusOne(self, digits):
        if digits==[]:digits.append(1)
        if digits[-1] in range(0,8):
            digits[-1]+=1
        else:
            digits.pop()
            digits.append(0)
            if len(digits)==1:digits.insert(0,1)
            if digits==[1,0]:return digits
            self.plusOne(digits[0:-1])
        return digits
s1 = Solution()
l=[9,9,9]
print(s1.plusOne(l))
        
