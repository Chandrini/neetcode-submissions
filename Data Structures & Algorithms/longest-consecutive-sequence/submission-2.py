class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        news=set(nums)
        longest=0
        for n in nums:
            if (n-1) not in news:
                length=1
            
                while (n+length) in news:
                    length+=1
            
                longest=max(length,longest)
        
        return longest

