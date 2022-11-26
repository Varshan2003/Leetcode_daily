class Solution:
    def generate(self, numRows):
        res = [[1]]
        for i in range(numRows):
            temp = [0]+res[-1]+[0]
            row = []
            for j in range(len(res[-1])+1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res

s1 = Solution()
print(s1.generate(5))