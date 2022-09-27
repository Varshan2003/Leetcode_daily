class Solution:
    def topKFrequent(self, nums,k):
        lst = sorted(nums)
        map2= {}
        for i in lst:
            if i in map2:
                map2[i]+=1
            else:
                map2[i]=1
        map1 = sorted(map2.values())
        ans1 = []
        ans2=[]
        for j in range(k):
            ans1.append(map1[-1-j])
        for key,value in map2.items():
            for x in ans1:
                if x==value:
                    ans2.append(key) 
                    break          
        return ans2
s1=Solution()
print(s1.topKFrequent([1,2],2))