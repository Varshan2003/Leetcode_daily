# from cmath import sqrt


# class Solution:
#     def kClosest(self, points, k):
#         dic ,temp = {},[]
#         for i in points:
#             res = pow(((i[0])*(i[0]))+((i[1])*(i[1])),0.5)
#             temp.append(res)
#             dic[res]=i
#             temp.sort()
#         ans = []
#         for i in range(k):
#             ans.append(dic[temp[i]])
#         return ans

# s1 = Solution()
# print(s1.kClosest(points =[[2,2],[2,2],[3,3],[2,-2],[1,1]]
# , k = 4))        

import heapq

class Solution:
    def kClosest(self, points, k):
        ans=[]
        for x,y in points:
            res = (x**2)+(y**2)
            ans.append([res,x,y])
        heapq.heapify(ans)
        fin = []
        for i in range(k):
            res1,x,y=heapq.heappop(ans)
            fin.append([x,y])
        return fin

s1 = Solution()
print(s1.kClosest(points =[[2,2],[2,2],[3,3],[2,-2],[1,1]], k = 4))        

