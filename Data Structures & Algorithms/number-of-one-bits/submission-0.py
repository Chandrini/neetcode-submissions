class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        num=bin(n)
        for i in num:
            if i=="1":
                cnt+=1
        return cnt