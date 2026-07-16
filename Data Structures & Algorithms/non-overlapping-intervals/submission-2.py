class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        removal=0
        last_end=float('-inf')
        intervals.sort(key=lambda x:x[1])

        for start,end in intervals:
            if start>=last_end:
                last_end=end
            
            else:
                removal+=1
        return removal