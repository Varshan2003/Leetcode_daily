class Solution:
    def leastBricks(self, wall):
        # maxE = 0
        # for i in wall:
        #     maxE = max(maxE,len(i))
        # finM = 1000000
        # for j in range(maxE):
        #     newM= 0
        #     for k in wall:
        #         if j<len(k):
        #             newM+=k[j]
        #     finM = min(newM,finM)
        # return finM
        Hm = {0:0}
        for r in wall:
            total = 0
            for b in r[:-1]:
                total+=b
                Hm[total] = 1+Hm.get(total,0)
        return len(wall)-max(Hm.values())
        
s1 = Solution()
print(s1.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))

