class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        nums.sort()
        def backtrack(i,sol):
            if i==len(nums):
                if sol not in res:
                    res.append(sol[:])
                return
    
            sol.append(nums[i])
            backtrack(i+1,sol)
            sol.pop()
            backtrack(i+1,sol)

        backtrack(0,[])
        return res

