class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        temp = 0
        prev = 0
        for i in range(len(bank)):
            temp = 0
            for j in range(len(bank[0])):
                if bank[i][j]=="1":
                    temp+=1
            total+=(prev*temp)
            if temp!=0:
                prev = temp
        return total

        