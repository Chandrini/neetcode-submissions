class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        for i in range(l):
            for j in range(l):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        return ([i,j])
