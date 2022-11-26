from unittest import result


class Solution:
    def lastStoneWeight(self, stones):
        stones1 = stones
        stones1.sort()
        while len(stones1)>1:
            result = stones1.pop() - stones1.pop()
            if result!=0:
                stones1.append(result)
            stones1.sort()
        return stones1[0] if len(stones1)==1 else 0
s1 = Solution()
print(s1.lastStoneWeight([2,2]))
