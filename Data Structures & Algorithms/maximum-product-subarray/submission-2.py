class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax=nums[0]
        curmin=nums[0]
        res=nums[0]

        
        for i in range(1,len(nums)):
            if nums[i]<0:
                curmax,curmin=curmin,curmax
            curmax=max(nums[i],curmax*nums[i])
            curmin=min(nums[i],curmin*nums[i])

            res=max(res,curmax)
        
        return res