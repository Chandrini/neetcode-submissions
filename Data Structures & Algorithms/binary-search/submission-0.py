class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def binary(low,high):
            while low<=high:
                mid=(low+high)//2
                
                if nums[mid]>target:
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    return mid
            return -1
        return binary(0,len(nums)-1)