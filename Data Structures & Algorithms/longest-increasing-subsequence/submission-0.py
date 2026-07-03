class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis=[1]*len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if i!=j:
                    if nums[i]>nums[j]:
                        lis[i]=max(lis[j]+1,lis[i])
        
        return max(lis)
