class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={j:0 for j in nums}
        for n in nums:
            if n not in d:
                d[n]=1
            else:
                d[n]+=1
        l=[]
        for i in range(k):
            x=max(d,key=d.get)
            l.append(x)
            del d[x]
        
        return l
