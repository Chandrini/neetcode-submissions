class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new=set()
        for ch in nums:
            if ch in new:
                return True
            else:
                new.add(ch)
        return False