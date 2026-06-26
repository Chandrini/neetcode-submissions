class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]
        def backtrack(open,close,i,s):
            if open==n and close==n:
                res.append(s)
                return 
            
            if open<n:
                backtrack(open+1,close,i+1,s+"(")
            if close<open:
                backtrack(open,close+1,i+1,s+")")
        backtrack(0,0,0,"")
        return res         



