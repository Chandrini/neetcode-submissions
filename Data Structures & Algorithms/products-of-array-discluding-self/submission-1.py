class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        output=[1]*l
        pref=[1]*l
        suff=[1]*l
        
        for i in range(1,l):
            pref[i]=pref[i-1]*nums[i-1]

        for j in range(l-2,-1,-1):
            suff[j]=suff[j+1]*nums[j+1]




        for i in range(len(nums)):
            output[i]=pref[i]*suff[i]
        
        return output
